import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.stats as stats

from strategy import strategy

# Import data
df = yf.download('ETH-USD', start = '2020-12-1', interval = '60m') # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

df = strategy(df, 0.0015, 12)


#plt.figure()
#df[['ret', 'strat']].cumprod().plot()
#plt.show()

#np.exp(df[['log_ret', 'log_strat']].cumsum()).plot()
#df[['log_ret', 'log_strat']].cumsum().plot()
