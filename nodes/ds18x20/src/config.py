class Config:

    # Wifi Config
    WIFI_SSID = ''                # SSID of the Wifi to log in
    WIFI_PASSWORD = ''            # Password of the Wifi

    # MQTT Config
    MQTT_SERVER = ''              # Address of the MQTT Broker.
    MQTT_PORT = 8883              # Port of the MQTT Broker (default=1883, ssl=8883)
    MQTT_USER = ''                # Username for the MQTT Broker if authentification is required
    MQTT_PASSWORD = ''            # Password for the MQTT Broker if authentification is required
    MQTT_SSL = True               # Use SSL connection to the broker. Set the port to 8883 if using SSL.
    MQTT_CERTFILE = None          # (SSL only) The certification file for the SSL connection
    MQTT_CLIENT_ID = ''           # The MQTT client id of the node
    MQTT_TOPIC = ''               # The  MQTT topic of the node

    # onewire
    ONEWIRE_PIN = 0               # Pin number for the onewire port

    # deepsleep
    ENABLE_DEEPSLEEP = True     # Enter deepsleep while waiting
    SLEEP_TIME_S = 60             # time between two measurements


config = Config()
