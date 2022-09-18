import os, socket, sys, textwrap, yaml

"""
todo - add error checking
"""

config_path = 'config.yaml'

def get_inputs():
    """
    get inputs - destination station, message
    """
    if len(sys.argv) < 2:
        dest = input("Destination Station: ")
        message = input("Message: ")
    else:
        dest = sys.argv[1]
        message = sys.argv[2]
    return dest, message

def config_parse(config_path):
    """
    parse yaml config file for callsign, passcode, server details
    """
    if not os.path.isfile(config_path): 
        sys.exit("Error: Config file " + config_path + "is missing. Please create it.")
    with open(config_path, 'r') as file:
        config_file = yaml.safe_load(file)
    callsign = config_file['your_station_info']['callsign']
    aprs_passcode = config_file['your_station_info']['aprs_passcode']
    server_host = config_file['aprs_server']['server_host']
    server_port = config_file['aprs_server']['server_port']
    return callsign, aprs_passcode, server_host, server_port

def packet_cons(callsign, aprs_passcode, dest, message):
    """
    construct multiline packet
    """
    address = callsign + ">APRS,TCPIP::"
    login = "user " + callsign + " pass " + str(aprs_passcode) + " vers aprs_send 1.0"
    final_dest = dest.ljust(9)
    packet = address + final_dest + ":" + message 
    ml_packet = textwrap.dedent(f"""
    {login}
    {packet}
    """)
    return ml_packet

def send_message(ml_packet, server_host, server_port):
    """
    open socket to local aprs.is server, send packet, hold open for 10s
    """
    print("\nPacket to be sent:", ml_packet)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((server_host, server_port))
    s.sendall(ml_packet.encode())
    while 1:
        try:
            data = s.recv(4096)
            print ("Received:", data.decode())
        except socket.timeout:
            print("Connection Closed")
            s.close()
            break

def main():
    dest,message = get_inputs()
    callsign,aprs_passcode,server_host,server_port = config_parse(config_path)
    ml_packet = (packet_cons(callsign, aprs_passcode, dest, message))
    send_message(ml_packet, server_host, server_port)


if __name__ == "__main__":
    main()

"""
credit: 
https://www.aprs-is.net/Connecting.aspx for technical spec
https://github.com/wa1gov/Simple-Shell-APRS/ for bash reference implementation
https://aprs.fi for cloud APIs and testing tools
"""