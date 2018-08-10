import sys
import json
import forecastio
import datetime
import time
with open('cities.json') as f:
    data = json.load(f)



api_key = 'ba6bb9549e9fc6be2c0cd11e973c9c27'
dtEast2 = datetime.datetime.today()
timeNow = dtEast2.strftime('%B %d, %Y, %I:%M %p')

def main():
    getLatLong()

def sleepySleeps():
    time.sleep(1)
    print('Searching... please wait.')
    time.sleep(1)

def getLatLong():
    uI = input('Enter a city to search: ')
    x = 0
    sleepySleeps()
    for c in data['cities']:
        try:
            if c['city'].lower() in uI.lower():
                x += 1
                userLat = c['latitude']
                userLong = c['longitude']
                forecast = forecastio.load_forecast(api_key, userLat, userLong)
                byDay = forecast.daily()
                byCurr = forecast.currently()

                byHour = forecast.hourly()
                byMinute = forecast.minutely()
                byAlert = forecast.alerts()
                

                print('\n---Weather Information for %s---'% uI.title())
                print('Time: %s'% timeNow)
                print('Current Temperature: %d°F'% byCurr.temperature)
                print('Daily Summary: %s'% byDay.summary)
                print('\n')
                break
        except:
            print('No matches found')
    if x == 0:
        print('Not Found')

if __name__ == '__main__':
    sys.exit(main())
