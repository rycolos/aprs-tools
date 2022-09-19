import datetime, json, requests, sys, yaml

"""
todo
"""

config_path = 'config.yaml'
url = 'https://api.aprs.fi/api/get?'


def get_inputs():
    #Get inputs. Check for cli params; if not found, take input.
    if len(sys.argv) < 2:
        dest = input('Station: ')
    else:
        dest = sys.argv[1]
    return dest


def config_parse(config_path):
    #Parse yaml config file for api key.
    try:
        with open(config_path, 'r') as file:
            config_file = yaml.safe_load(file)
    except FileNotFoundError as e:
        print(f'File {config_path} not found. Exiting.')
        sys.exit(1)
    try:    
        api_key = config_file['aprs_fi']['api_key']
    except KeyError as e:
        print(f'Config missing key: {e}. Exiting.')
        sys.exit(1)
    return api_key


def api_read(url, dest, api_key):
    #Construct query params, read from aprs.fi api.
    params = {
        'what': 'msg',
        'dst': dest,
        'apikey': api_key,
        'format': 'json'
    }
    try:
        resp = requests.get(url=url, params=params)
    except requests.exceptions.RequestException as e:
        print(f'API error: {e}')
        sys.exit(1)
    data = resp.json()
    entries = data.get('entries')
    count = data.get('found')
    if entries == None or entries == []:
        print('Station not found or bad API credentials.')
        sys.exit(1)
    return entries, count



def tz_convert(entries):
    #Convert unix ts to local tz.
    for item in entries:
        ts = int(item['time'])
        item['time'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def main():
    dest = get_inputs()
    api_key = config_parse(config_path)
    entries,count = api_read(url, dest, api_key)
    tz_convert(entries)
    print(f'Displaying {count} most recent messages \n')
    for item in entries:
        print(item)


if __name__ == '__main__':
    main()