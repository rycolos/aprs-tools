import socket, sys

#GET DESTINATION + MESSAGE
if len(sys.argv) < 2:
    dest = input("Destination Station: ")
    message = input("Message: ")
else:
    dest = sys.argv[1]
    message = sys.argv[2]

#CONFIG - edit these
callsign = "KC1QBY-1"
password = "19369"
serverHost = "noam.aprs2.net"
serverPort = 14580

#CONFIG PARSE
address = callsign + ">APRS,TCPIP::"
login = "user " + callsign + " pass " + password + " vers aprs_send 1.0"
final_dest = dest.ljust(9)
packet = address + final_dest + ":" + message 
ml_packet = f"""
{login}
{packet}
"""

#SOCKET
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