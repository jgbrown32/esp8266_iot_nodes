# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
from config import config
import main
import core

global wifi, mqtt

# Connect Wifi
wifi = core.WifiWrapper(config)
wifi.connect()

# Connect MQTT
mqtt = core.MQTTClientWrapper(config)
mqtt.connect()

main.run()
