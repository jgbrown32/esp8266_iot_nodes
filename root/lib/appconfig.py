from credentials import WifiConfig, MQTTConfig
# import credentials


class Config(WifiConfig, MQTTConfig):

    MQTT_CLIENT_ID = 'hcscr501node'
    MQTT_TOPIC = 'home/hcsr501'

    ENABLE_DEEPSLEEP = False

    PIN_SENSOR = 5  # Pin for reading the sensor.  D1 = GPIO5

config = Config()
