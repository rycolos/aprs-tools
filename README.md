# APRS-tools
The [Automated Packet Reporting System (APRS)](http://www.aprs.org) is a packet radio mode for amateur operators that enables the transmission and reception of location, weather, alerts, bulletins, messages and other data through digitally encoded signals, predominantly on the VHF bands.

aprs-tools is a small collection of scripts that enable cli input and output from the [Automatic Packet Reporting System-Internet Service (APRS-IS)](http://www.aprs-is.net). Functions include: (1) enabling a station to send a message via an APRS-IS server directly to another station; (2) querying a station for its latest location and other station data; and (3) querying a station's most recent 10 messages.
## Installation
Requires Python 3. See requirements.txt for other dependencies.

Using git:
```
cd
git clone https://github.com/rycolos/aprs-tools.git
cd aprs-tools
```
Using wget:
```
cd
wget https://github.com/rycolos/aprs-tools/archive/refs/heads/main.zip
unzip main.zip
cd aprs-tools
```
Install dependencies:
```
pip3 install -r requirements.txt
```
## Configuration
Rename `config.yaml.template` to `config.yaml` and add the relevant values.
* *callsign* - Your station callsign. Used as the sending station in `aprs_sender`.
* *aprs_passcode* - Your stations' APRS-IS passcode. See <https://apps.magicbug.co.uk/passcode/> to generate a passcode if you do not have one already. Used in `aprs_sender`.
* *server_host* - Your local APRS-IS server. See <http://www.aprs-is.net/APRSServers.aspx> for a list of servers. Used in `aprs_sender`.
* *server_port* - APRS-IS server port. 14580 is defined in the APRS-IS spec. You probably won't want to change this. Used in `aprs_sender`.
* *api_key* - API key for aprs.fi. Requires an aprs.fi account. See <https://aprs.fi/page/api>. Used in `aprs_query` and `aprs_msg_check`.
## aprs-sender
Send a message via an APRS-IS server to a destination APRS station.
### Usage
Requires destination state and message. These can be either passed as a parameter when running the script or via interactive input.
```
> python3 aprs_sender.py CALLSIGN test message

> python3 aprs_sender.py
Destination Station: CALLSIGN
Message: test message
```
### Example
```
> python3 aprs_sender.py
Destination Station: CALLSIGN
Message: test message

Packet to be sent:
 
user CALLSIGN pass XXXXXX vers aprs_tools 1.0
CALLSIGN>APRS,TCPIP::CALLSIGN :test message

Received: # aprsc 2.1.11-g80df3b4

Received: # logresp CALLSIGN verified, server T2VAN

Connection Closed
```
## aprs_query
Query aprs.fi for basic station information.
### Usage
Requires target station. This can be either passed as a parameter when running the script or via an interactive input.
```
> python3 aprs_query.py CALLSIGN

> python3 aprs_sender.py
Station: CALLSIGN
```
### Example
```
> python3 aprs_query.py
Station: CALLSIGN
class a
name CALLSIGN
type l
time 2022-09-08 06:45:59
lasttime 2022-09-19 06:52:13
lat 44.28683
lng -70.524
symbol R&
srccall CALLSIGN
dstcall APDW16
phg 2040
comment RPi Zero + Direwolf iGate
path TCPIP*,qAC,T2MCI
```
### Description (from aprs.fi docs)
* class - class of station identifier (a: APRS, i: AIS, w: Web ...)
* name - name of station, object, item or vessel
* showname - displayed name of station (may differ from the unique name)
* type - type of target: a for AIS, l for APRS station, i for APRS item, o for APRS object, w for weather station
* time - the time when the target first reported this (current) position (the time of arrival at current * coordinates)
* lasttime - the time when the target last reported this (current) position
* lat - latitude in decimal degrees, north is positive
* lng - longitude in decimal degrees, east is positive
* course - Course over ground / COG, in degrees
* speed - Speed, in kilometers per hour
* altitude - Altitude, in meters
* symbol - APRS symbol table and code
* srccall - Source callsign - either APRS source callsign or AIS vessel callsign
* dstcall - APRS packet destination callsign
* comment - APRS comment or AIS destination and estimated time of arrival
* path - APRS or AIS packet path
* phg - APRS PHG value
* status - Last status message transmitted by station
* status_lasttime - The time when the last status message was received
Please respect [aprs.fi terms](https://aprs.fi/page/api) especially with regards to query rates.
## aprs_msg_check
Query aprs.fi for the 10 most recent messages sent to a station. This can be either passed as a parameter when running the script or via an interactive input.
### Usage
```
> python3 aprs_msg_check.py CALLSIGN

> python3 aprs_sender.py
Station: CALLSIGN
```
### Example
```
> python3 aprs_msg_check.py
Station: CALLSIGN
Displaying 2 most recent messages 

{'messageid': '82180175', 'time': '2022-09-19 07:07:50', 'srccall': 'CALLSIGN', 'dst': 'CALLSIGN, 'message': 'test message'}
{'messageid': '82178723', 'time': '2022-09-19 05:48:34', 'srccall': 'CALLSIGN', 'dst': 'CALLSIGN', 'message': 'test message 2'}
```
### Description (from aprs.fi docs)
* messageid - an incrementing id of the message (will wrap to 0 some day)
* time - Time when the message was received
* srccall - Source callsign
* dst - APRS message destination
* message - The message contents
Please respect [aprs.fi terms](https://aprs.fi/page/api) especially with regards to query rates.
## Credits 
* <https://www.aprs-is.net/Connecting.aspx> for technical spec.
* <https://github.com/wa1gov/Simple-Shell-APRS/> for reference implementation in bash.
* <https://aprs.fi> for cloud APIs and testing tools.

