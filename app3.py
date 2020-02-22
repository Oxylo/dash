import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2020, 2, 10)

df = web.DataReader('GDP', 'fred', start, end)

print(df.head(10))
