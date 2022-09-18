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
    params = {'what': 'msg', 'dst': dest, 'apikey': api_key, 'format': 'json'}
    resp = requests.get(url=url, params=params)
    data = resp.json()
    entries = data.get('entries')
    count = data.get('found')
    return entries, count

def tz_convert(entries):
    """
    convert unix ts to local tz
    """
    for item in entries:
        ts = int(item['time'])
        item['time'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def main():
    dest = get_inputs()
    api_key = config_parse(config_path)
    entries,count = api_read(url, dest, api_key)
    tz_convert(entries)

    print("Displaying", count, "most recent messages.\n")
    for item in entries:
        print(item)

if __name__ == "__main__":
    main()