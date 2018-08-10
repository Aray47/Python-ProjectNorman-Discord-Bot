from darksky import forecast
from datetime import date, timedelta

BOSTON = 42.3601, 71.0589

weekday = date.today()
with forecast('ba6bb9549e9fc6be2c0cd11e973c9c27', *BOSTON) as boston:
    print(boston.daily.summary, end='\n---\n')
    for day in boston.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax
                   )
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
        weekday += timedelta(days=1)