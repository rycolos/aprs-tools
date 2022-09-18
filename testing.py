import os, sys, yaml

def config_parse():
    config_path = 'config.yaml'
    if not os.path.isfile(config_path): 
        sys.exit("Error: Config file " + config_path + "is missing. Please create it.")
    with open(config_path, 'r') as file:
        config_file = yaml.safe_load(file)
    callsign = config_file['your_station_info']['callsign']
    aprs_passcode = config_file['your_station_info']['aprs_passcode']
    timezone = config_file['your_station_info']['timezone']
    server_host = config_file['aprs_server']['server_host']
    server_port = config_file['aprs_server']['server_port']
    return callsign, aprs_passcode, timezone, server_host, server_port

callsign,aprs_passcode,timezone,server_host,server_port = config_parse()
print(callsign)
