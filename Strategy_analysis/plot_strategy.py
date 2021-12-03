import yfinance as yf
import matplotlib.pyplot as plt

from strategy import strategy

# Edit the strategy here
trigger = 0.005
window = 11
start_date = '2021-10-1'

df = yf.download('ETH-USD', start = start_date, interval = '1d') # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
df = strategy(df, trigger, window)

vol = df[['log_ret','log_strat']].std()*len(df)**.5 * 100

# Print and Plot Results
print('Number of trades in period: ', int(df['trades'].tail(1)))
print('Percent of time in long position: ', sum(df['position'])/len(df['position'])*100 , '%')
print('Asset Volatility: ', vol['log_ret']*100, '%')
print('Strategy Volatility: ', vol['log_strat']*100, '%')

data_to_plot = (df[['Asset return', 'Strategy return']].cumprod()-1) * 100
data_to_plot[['Asset return', 'Strategy return']].plot()
#df['trades'].plot()

plt.title('Momentum Strategy ETH-USD\nTrigger: 0.005, Window: 11 days')
plt.ylabel('Return (%)')

plt.grid(visible=True)
plt.show()