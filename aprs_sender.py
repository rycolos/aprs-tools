import socket, sys, textwrap

#CONFIG STATION AND SERVER - edit these
callsign = "KC1QBY-1" #your station callsign
passcode = "19369" #https://apps.magicbug.co.uk/passcode/
serverHost = "noam.aprs2.net" #choose local server
serverPort = 14580 #defined in aprs-is spec

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

def config_parse(callsign, passcode, message):
    """
    parse to multiline packet
    """
    address = callsign + ">APRS,TCPIP::"
    login = "user " + callsign + " pass " + passcode + " vers aprs_send 1.0"
    final_dest = dest.ljust(9)
    packet = address + final_dest + ":" + message 
    ml_packet = textwrap.dedent(f"""
    {login}
    {packet}
    """)
    return ml_packet

def send_message(ml_packet, serverHost, serverPort):
    """
    open socket to local aprs.is server, send packet, hold open for 10s
    """
    print("Packet to be sent:", ml_packet)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((serverHost, serverPort))
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
    ml_packet = (config_parse(callsign, passcode, message))
    send_message(ml_packet, serverHost, serverPort)


if __name__ == "__main__":
    main()


#credit: https://www.aprs-is.net/Connecting.aspx, simpleaprs