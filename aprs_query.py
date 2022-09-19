import datetime, json, os, requests, sys, yaml

"""
todo - error checking
"""

config_path = 'config.yaml'
url = 'https://api.aprs.fi/api/get?'


def get_inputs():
    """
    get inputs - target station
    """
    if len(sys.argv) < 2:
        dest = input("Station: ")
    else:
        dest = sys.argv[1]
    return dest


def config_parse(config_path):
    """
    parse yaml config file for api key
    """
    if not os.path.isfile(config_path): 
        sys.exit("Error: Config file " + config_path + "is missing. Please create it.")
    with open(config_path, 'r') as file:
        config_file = yaml.safe_load(file)
    api_key = config_file['aprs_fi']['api_key']
    return api_key


def api_read(url, dest, api_key):
    """
    construct query params, read from aprs.fi api
    """
    params = {'name': dest, 'what': 'loc', 'apikey': api_key, 'format': 'json'}
    resp = requests.get(url=url, params=params)
    data = resp.json()
    entries = data.get('entries')
    return entries


def tz_convert(entries):
    """
    convert unix ts to local tz
    """
    ts_time = int(entries[0].get('time'))
    entries[0]['time'] = datetime.datetime.fromtimestamp(ts_time).strftime('%Y-%m-%d %H:%M:%S')

    ts_lasttime = int(entries[0].get('lasttime'))
    entries[0]['lasttime'] = datetime.datetime.fromtimestamp(ts_lasttime).strftime('%Y-%m-%d %H:%M:%S')


def main():
    dest = get_inputs()
    api_key = config_parse(config_path)
    entries = api_read(url, dest, api_key)
    tz_convert(entries)
    
    for key,value in entries[0].items():
        print(key,value)


if __name__ == "__main__":
    main()