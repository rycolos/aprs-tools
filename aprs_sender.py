import socket, sys, textwrap, yaml

"""
todo:
"""

config_path = 'config.yaml'


def get_inputs():
    #Get inputs. Check for cli params; if not found, take input.
    if len(sys.argv) < 2:
        dest = input('Destination Station: ')
        message = input('Message: ')
    else:
        dest = sys.argv[1]
        message = sys.argv[2]
    return dest, message


def config_parse(config_path):
    #Parse yaml config file for callsign, passcode, server details.
    try:
        with open(config_path, 'r') as file:
            config_file = yaml.safe_load(file)
    except FileNotFoundError as e:
        print(f'File {config_path} not found. Exiting.')
        sys.exit(1)
    try:
        callsign = config_file['your_station_info']['callsign']
        aprs_passcode = str(config_file['your_station_info']['aprs_passcode'])
        server_host = config_file['aprs_server']['server_host']
        server_port = config_file['aprs_server']['server_port']
    except KeyError as e:
        print(f'Config missing key: {e}. Exiting.')
        sys.exit(1)
    return callsign, aprs_passcode, server_host, server_port


def packet_cons(callsign, aprs_passcode, dest, message):
    #Construct multiline packet.
    address = f'{callsign}>APRS,TCPIP::'
    login = f'user {callsign} pass {aprs_passcode} vers aprs_tools 1.0'
    final_dest = dest.ljust(9)
    packet = f'{address}{final_dest}:{message}'
    ml_packet = textwrap.dedent(f"""
    {login}
    {packet}
    """)
    return ml_packet


def send_message(ml_packet, server_host, server_port):
    #Open socket to local aprs.is server, send packet, hold open for 10s.
    print(f'\nPacket to be sent:\n {ml_packet}')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((server_host, server_port))
        s.sendall(ml_packet.encode())
    except socket.error as e:
        print(f'Error connecting to {server_host} at port {server_port}')
        sys.exit(1)
    while True:
        try:
            data = s.recv(4096)
            print(f'Received: {data.decode()}')
        except socket.timeout:
            print('Connection Closed')
            s.close()
            break


def main():
    dest, message = get_inputs()
    callsign, aprs_passcode, server_host, server_port = config_parse(config_path)
    ml_packet = (packet_cons(callsign, aprs_passcode, dest, message))
    send_message(ml_packet, server_host, server_port)


if __name__ == '__main__':
    main()