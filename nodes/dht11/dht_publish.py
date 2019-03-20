from time import sleep
import umqtt.simple
import machine
import dht
import sys

def main():
  SERVER = '192.168.1.222'
  CLIENT_ID = 'ESP8266_DHT11_Sensor'
  TOPIC = 'temp_humidity'

  client = umqtt.simple.MQTTClient(CLIENT_ID, SERVER)
  try:
      client.connect()
      print("MQTT connected...")
  except:
      print("MQQT could not connect")
      sys.exit(1)

  sensor = dht.DHT11(machine.Pin(2))

  while True:
    try:
      sensor.measure()
      t = sensor.temperature()
      h = sensor.humidity()
      if isinstance(t, int) and isinstance(h, int):  #Confirm good data received.
#        msg = ('{0:3.1f}C, {1:3.1f}'.format(t, h))
        msg = ('{0:3.1f}F, {1:3.1f}'.format(32.0 + 1.8 * t, h))
        client.publish(TOPIC, msg)
        print(msg)
      else:
        print('Invalid sensor readings.')
    except OSError:
      print('Faild to read sensor.')
    sleep(60)
