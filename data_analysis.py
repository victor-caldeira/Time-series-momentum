import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from strategy import strategy

# Import data
df = yf.download('ETH-USD', start = '2020-11-29', interval = '60m')

df = strategy(df, 0.0015, 12)
#print(df)

#plt.figure()
#df[['ret', 'strat']].cumprod().plot()
#plt.show()

#np.exp(df[['log_ret', 'log_strat']].cumsum()).plot()
#df[['log_ret', 'log_strat']].cumsum().plot()
