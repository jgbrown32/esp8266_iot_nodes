# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
from sysconfig import sysconfig
import core

global wifi, mqtt

# Connect Wifi
wifi = core.WifiWrapper(sysconfig)
wifi.connect()

# Connect MQTT
mqtt = core.MQTTClientWrapper(sysconfig)
try:
    mqtt.connect()
    print("MQTT connected...")
# Publish mqtt connection status to system topic.
#    msg = ('jgb-esp8266-52 MQTT connected')
#    mqtt.publish(SYS_TOPIC, msg)
except:
    print("MQQT could not connect")
    sys.exit(1)
