# APRS-tools
## Installation
## Using aprs-tools
### Configuration
Rename `config.yaml.template` to `config.yaml` and add the relevant values.
* *callsign* - Your station callsign. Used as the sending station in `aprs_sender`.
* *aprs_passcode* - Your stations' APRS-IS passcode. See <https://apps.magicbug.co.uk/passcode/> to generate a passcode if you do not have one already. Used in `aprs_sender`.
* *server_host* - Your local APRS-IS server. See <http://www.aprs-is.net/APRSServers.aspx> for a list of servers. Used in `aprs_sender`.
* *server_port* - APRS-IS server port. 14580 is defined in the APRS-IS spec. You probably won't want to change this. Used in `aprs_sender`.
* *api_key* - API key for aprs.fi. Requires an aprs.fi account. See <https://aprs.fi/page/api>. Used in `aprs_query` and `aprs_msg_check`.
### aprs-sender
Send a message via an APRS-IS server to a destination APRS station.
#### Usage
```
usage
```
#### Example
```
example
```
### aprs_query
Query aprs.fi for basic station information.
#### Usage
```
usage
```
#### Example
```
example
```
#### Description (from aprs.fi docs)
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
### aprs_msg_check
Query aprs.fi for the 10 most recent messages sent to a station.
#### Usage
```
usage
```
#### Example
```
example
```
#### Description (from aprs.fi docs)
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

