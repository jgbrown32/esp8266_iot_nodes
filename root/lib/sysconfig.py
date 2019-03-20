# sysconfig.py - System Constants and Variables
##
from credentials import WifiCredConfig, MQTTCredConfig

class WifiConfig:

    # WIFI constants
    WIFI_MAX_RETRIES = 3        # number of retries before reset
    WIFI_TIMEOUT_MS = 10000     # timout value for Wifi connection

    # WIFI variables
    WIFI_DHCP_HOSTNAME = ''     # Optional: Network host name.
    # Network addresses for setting static IP address.  If blank, dynamic IP is used.
    WIFI_IP_ADDRESS = ''        # Optional: Static IP address to assign to host.
    WIFI_SUBNET_MASK = ''       # Optional: Network subnet mask.
    WIFI_GATEWAY = ''           # Optional: Network gateway.
    WIFI_DNS_SERVER = ''        # Optional: Network DNS server.


class MQTTConfig:

    # MQTT constants
    MQTT_MAX_RETRIES = 3        # maximum retries before reset

    # MQTT variables
    MQTT_SERVER = ''            # ip or domain of the mqtt broker
    MQTT_CLIENT_ID = ''         # ID to associate with this MQTT client.
    MQTT_SYS_TOPIC = ''         # MQTT system topic to report/recieve system status and config.
    MQTT_PORT = 1883            # port for mqtt connection (e.g. 1883, 8883)
    MQTT_KEEPALIVE = 0          # keepalive value in seconds for MQTT connect, 0 if disabled

    # ssl
    MQTT_SSL = False            # true if SSL enable, change the port to 8883 then
    MQTT_CERTFILE = None        # filename of the certfile for SSL connection
    MQTT_SSL_PARAMS = {}        # additional SSL parameters


class MQTTConfigSSL(MQTTConfig):

    MQTT_SSL = True
    MQTT_PORT = 8883
