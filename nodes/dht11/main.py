def do_connect():
  import network
  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  if not sta_if.isconnected():
    print('Connecting to network...')
    sta_if.config(dhcp_hostname= "jgb-ESP8266-50")
    sta_if.ifconfig(('192.168.1.50', '255.255.255.0', '192.168.1.1', '75.75.75.75'))
    sta_if.connect("jgbrown", "4t9j1jdihn28nz32")
    while not sta_if.isconnected():
      pass
  print('Network Configuration: ', sta_if.ifconfig())

do_connect()
