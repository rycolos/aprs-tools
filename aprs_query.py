import datetime, json, os, requests, sys, yaml

script_dir = os.path.dirname(__file__)
config_path = f'{script_dir}/config.yaml'

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
        'name': dest, 
        'what': 'loc', 
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
    if entries == None or entries == []:
        print('Station not found or bad API credentials.')
        sys.exit(1)
    return entries


def tz_convert(entries):
    #Convert unix ts to local tz.
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


if __name__ == '__main__':
    main()