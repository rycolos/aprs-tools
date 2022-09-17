import datetime, json, requests, sys

#GET STATION
if len(sys.argv) < 2:
    dest = input("Station: ")
else:
    dest = sys.argv[1]

api_key = '175190.00oQHakWkWa4M'

url = 'https://api.aprs.fi/api/get?name=' + dest + '&what=loc&apikey=' + api_key + '&format=json'

resp = requests.get(url=url)
data = resp.json()
entries = data.get('entries')

#CONVERT UNIX TS
ts_time = int(entries[0].get('time'))
entries[0]['time'] = datetime.datetime.fromtimestamp(ts_time).strftime('%Y-%m-%d %H:%M:%S')
ts_lasttime = int(entries[0].get('lasttime'))
entries[0]['lasttime'] = datetime.datetime.fromtimestamp(ts_lasttime).strftime('%Y-%m-%d %H:%M:%S')

for key,value in entries[0].items():
    print(key,value)