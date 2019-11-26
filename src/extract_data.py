import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(1987,1,1)
end = dt.datetime(2019,11,20)
df = web.DataReader('TSLA', 'yahoo', start, end)

df.plot()
plt.show()
df.to_csv('TSLA.csv')