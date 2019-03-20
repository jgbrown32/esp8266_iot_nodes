import network
import utime
import machine
from umqtt.simple import MQTTClient


def sleep(sysconfig):
    if sysconfig.ENABLE_DEEPSLEEP:
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
        rtc.alarm(rtc.ALARM0, sysconfig.SLEEP_TIME_S * 1000)
        print('entering deepsleep ({} seconds)'.format(sysconfig.SLEEP_TIME_S))
        machine.deepsleep()
    else:
        print('sleeping for {} seconds.'.format(sysconfig.SLEEP_TIME_S))
        utime.sleep(sysconfig.SLEEP_TIME_S)


class WifiConnectionError(Exception):
    pass


class MQTTConnectionError(Exception):
    pass


class MQTTClientWrapper:

    def __init__(self, sysconfig):

        self.server = sysconfig.MQTT_SERVER
        self.port = sysconfig.MQTT_PORT
        self.mqtt_client = MQTTClient(
            client_id=sysconfig.MQTT_CLIENT_ID,
            server=self.server,
            port=self.port,
            user=sysconfig.MQTT_USER,
            password=sysconfig.MQTT_PASSWORD,
            keepalive=sysconfig.MQTT_KEEPALIVE,
            ssl=sysconfig.MQTT_SSL,
            ssl_params=sysconfig.MQTT_SSL_PARAMS,
        )
        self.mqtt_client.set_callback(self._process_incoming_msgs)
        self.callbacks = {}
        self.connected = False
        self.max_retries = MQTT_MAX_RETRIES

    def connect(self):
        attempt = 1
        while attempt <= self.max_retries:
            print('connecting to mosquitto server "{}:{}" (attempt {})...'
                  .format(self.server, self.port,
                          attempt), end='')

            try:
                res = self.mqtt_client.connect()
                if res == 0:
                    print('done')
                    break
                else:
                    print('error {}'.format(res))
                    attempt += 1

            except OSError:
                print('error')
                attempt += 1
        else:
            self.connected = False
            raise MQTTConnectionError()

        self.connected = True

    def disconnect(self):
        self.mqtt_client.disconnect()

    def publish(self, topic, msg, qos=0, retain=False):
        print('publishing topic {}: {}...'.format(topic, msg), end='')
        self.mqtt_client.publish(topic, msg, qos, retain)
        print('done')

    def subscribe(self, topic, callback):
        self.callbacks[topic] = callback
        self.mqtt_client.subscribe(topic)

    def _process_incoming_msgs(self, topic, msg):
        topic = topic.decode()
        msg = msg.decode()
        callback = self.callbacks.get(topic)
        if callback is not None:
            callback(topic, msg)

    def wait_msg(self):
        return self.mqtt_client.wait_msg()

    def check_msg(self):
        return self.mqtt_client.check_msg()

    def ping(self):
        return self.mqtt_client.ping()


class WifiWrapper:

    def __init__(self, sysconfig):
        self.ssid = sysconfig.WIFI_SSID
        self.password = sysconfig.WIFI_PASSWORD
        self.max_retries = WIFI_MAX_RETRIES
        self.timeout_ms = WIFI_TIMEOUT_MS
        self.ap_if = network.WLAN(network.AP_IF)
        self.sta_if = network.WLAN(network.STA_IF)

    def connect(self):
        attempt = 1

        if self.ap_if.active():
            self.ap_if.active(False)

        if not self.sta_if.isconnected():
            self.sta_if.active(True)
            while attempt <= self.max_retries:
                print('connecting to network "{}" (attempt {})...'
                      .format(self.ssid, attempt), end='')
                self.sta_if.connect(self.ssid, self.password)
                t0 = utime.ticks_ms()
                while not self.sta_if.isconnected():
                    if abs(utime.ticks_ms() - t0) > self.timeout_ms:
                        print('error')
                        print('wifi connection timed out')
                        attempt += 1
                        break
                else:
                    break
            else:
                raise WifiConnectionError()
        print('done')
        print('network sysconfig:', self.sta_if.ifsysconfig())

    @property
    def isconnected(self):
        return self.sta_if.isconnected()
