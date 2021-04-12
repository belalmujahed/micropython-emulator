STA_IF = "Station"
AP_IF = "Access Point"


class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are network.STA_IF (station aka client, connects to
    upstream WiFi access points) and network.AP_IF (access point, allows other WiFi clients to connect). Availability of
     the methods below depends on interface type. For example, only STA interface may WLAN.connect() to an access point.
    """

    def __init__(self, interface_id: str):
        self.interface_id_for_testing = interface_id

    def active(self, is_active: bool) -> bool:
        """
        Activate (“up”) or deactivate (“down”) network interface, if boolean argument is passed.
        Otherwise, query current state if no argument is provided. Most other methods require active interface.
        :return: is_active
        """
        return is_active

    def connect(self, ssid: str = None, password: str = None, *, bssid: str = None):
        """
        Connect to the specified wireless network, using the specified password.
        If bssid is given then the connection will be restricted to the access-point with that MAC address
        (the ssid must also be specified in this case).
        :param ssid: SSID name
        :param password: SSID Password
        :param bssid: BSSID
        :return: None
        """
        return None

    def disconnect(self):
        """
        Disconnect from the currently connected wireless network.
        :return: None
        """
        return None

    def scan(self) -> None:
        """
        Scan for the available wireless networks.

        Scanning is only possible on STA interface. Returns list of tuples with the information about WiFi access points:

        (ssid, bssid, channel, RSSI, authmode, hidden)

        bssid is hardware address of an access point, in binary form, returned as bytes object.
        You can use ubinascii.hexlify() to convert it to ASCII form.

        There are five values for authmode:

        0 – open

        1 – WEP

        2 – WPA-PSK

        3 – WPA2-PSK

        4 – WPA/WPA2-PSK

        and two for hidden:

        0 – visible

        1 – hidden
        :return: None
        """
        return None

    def status(self, param: str) -> str:
        """
        eturn the current status of the wireless connection.

        When called with no argument the return value describes the network link status. The possible statuses are defined as constants:

        STAT_IDLE – no connection and no activity,

        STAT_CONNECTING – connecting in progress,

        STAT_WRONG_PASSWORD – failed due to incorrect password,

        STAT_NO_AP_FOUND – failed because no access point replied,

        STAT_CONNECT_FAIL – failed due to other problems,

        STAT_GOT_IP – connection successful.

        When called with one argument param should be a string naming the status parameter to retrieve. Supported parameters in WiFI STA mode are: 'rssi'.
        :param:When called with one argument param should be a string naming the status parameter to retrieve.
        Supported parameters in WiFI STA mode are: 'rssi'.
        :return:STAT_IDLE – no connection and no activity,

                STAT_CONNECTING – connecting in progress,

                STAT_WRONG_PASSWORD – failed due to incorrect password,

                STAT_NO_AP_FOUND – failed because no access point replied,

                STAT_CONNECT_FAIL – failed due to other problems,

                STAT_GOT_IP – connection successful.
        """
        return ""

    def isconnected(self) -> bool:
        """
        In case of STA mode, returns True if connected to a WiFi access point and has a valid IP address.
        In AP mode returns True when a station is connected. Returns False otherwise.
        :return:
        """
        return True

    def ifconfig(
        self, ip: str = None, subnet: str = None, gateway: str = None, dns: str = None
    ) -> tuple:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask, gateway and DNS server.
        When called with no arguments, this method returns a 4-tuple with the above information.
        To set the above values, pass a 4-tuple with the required information. For example:

                        nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        :return: Tuple containing ip, subnet, gateway, dns
        """
        return ip, subnet, gateway, dns

    def config(self, param: str) -> str:
        """
        Get or set general network interface parameters. These methods allow to work with additional parameters
        beyond standard IP configuration (as dealt with by WLAN.ifconfig()). These include network-specific
        and hardware-specific parameters. For setting parameters, keyword argument syntax should be used, multiple
        parameters can be set at once. For querying, parameters name should be quoted as a string, and only one
        parameter can be queries at time:
        Parameter
        +---------------+-------------------------------------------------------------------+
        | Parameter     | Description                                                       |
        +---------------+-------------------------------------------------------------------+
        | mac           | MAC address (bytes)                                               |
        +---------------+-------------------------------------------------------------------+
        | essid         | WiFi access point name (string)                                   |
        +---------------+-------------------------------------------------------------------+
        | channel       | WiFi channel (integer)                                            |
        +---------------+-------------------------------------------------------------------+
        | hidden        | Whether ESSID is hidden (boolean)                                 |
        +---------------+-------------------------------------------------------------------+
        | authmode      | Authentication mode supported (enumeration, see module constants) |
        +---------------+-------------------------------------------------------------------+
        | password      | Access password (string)                                          |
        +---------------+-------------------------------------------------------------------+
        | dhcp_hostname | The DHCP hostname to use                                          |
        +---------------+-------------------------------------------------------------------+
        :return:  String with the requested parameter
        """
        return ""
