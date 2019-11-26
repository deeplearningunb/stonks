import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')

#date format: year/month/day 
start = dt.datetime(1987,1,1)
end = dt.datetime(2019,11,20)

# To get another stock information
# inform another stock name
df = web.DataReader('TSLA', 'yahoo', start, end)

df.plot()
plt.show()

#Remember to change the csv name
df.to_csv('TSLA.csv')