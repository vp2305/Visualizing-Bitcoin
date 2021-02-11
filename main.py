from math import log
from pandas.core.indexing import is_label_like
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto = "BTC"
currency = "CAD"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)
# plt.plot(data['Close'])
# plt.show()

plt.yscale("log")


plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc="upper left")
plt.show()

# mpf.plot(eth, type="candle", volume=True, style="yahoo")
# print(eth)
# mpf.plot(btc, type="candle", volume=True, style="yahoo")
# print(btc)
