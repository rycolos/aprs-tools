import datetime, json, requests, sys

#GET STATIONKC
if len(sys.argv) < 2:
    dest = input("Station: ")
else:
    dest = sys.argv[1]

api_key = '175190.00oQHakWkWa4M'

url = 'https://api.aprs.fi/api/get?what=msg&dst=' + dest + '&apikey=' + api_key + '&format=json'

resp = requests.get(url=url)
data = resp.json()
entries = data.get('entries')

print("Displaying", data.get('found'), "most recent messages.\n")

for item in entries:
    #CONVERT UNIX TS
    ts = int(item['time'])
    item['time'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    print(item)

