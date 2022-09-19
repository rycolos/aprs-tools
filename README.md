# APRS-tools
## Installation
## Using aprs-tools
### Configuration
Rename `config.yaml.template` to `config.yaml` and add the relevant values.
* callsign - Your station callsign. Used as the sending station in `aprs_sender`.
* aprs_passcode - Your stations' APRS-IS passcode. See <https://apps.magicbug.co.uk/passcode/> to generate a passcode if you do not have one already. Used in `aprs_sender`.
* server_host - Your local APRS-IS server. See <http://www.aprs-is.net/APRSServers.aspx> for a list of servers. Used in `aprs_sender`.
* server_port - APRS-IS server port. 14580 is defined in the APRS-IS spec. You probably won't want to change this. Used in `aprs_sender`.
* api_key - API key for aprs.fi. Requires an aprs.fi account. See <https://aprs.fi/page/api>. Used in `aprs_query` and `aprs_msg_check`.
### aprs-sender
### aprs_query
Please respect [aprs.fi terms](https://aprs.fi/page/api).
### aprs_msg_check
Please respect [aprs.fi terms](https://aprs.fi/page/api).
## Credits 
* https://www.aprs-is.net/Connecting.aspx for technical spec
* https://github.com/wa1gov/Simple-Shell-APRS/ for bash reference implementation
* https://aprs.fi for cloud APIs and testing tools

