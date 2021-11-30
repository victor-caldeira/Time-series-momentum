import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
#import scipy.stats as stats

from strategy import strategy

# Import data
df = yf.download('ETH-USD', start = '2020-12-1', interval = '1d') # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

# Run Strategy with different Triggers and windows
#dfs = []
results = pd.DataFrame(columns = ['trigger', 'window', 'return', 'volatility'])
for trigger in np.linspace(0, 0.02, 50):
    for window in np.linspace(10, 11, 1, dtype=int):
        df_i = strategy(df, trigger, window)
        #dfs.append(df_i)
        
        vol = df_i[['log_strat']].std()*len(df)**.5 * 100
        strat_ret = (df_i[['strat']].prod() - 1) * 100
        
        results.loc[len(results)] = [round(trigger,4) , window, float(strat_ret), float(vol)]

    print('Trigger ', round(trigger,4), ' calculated')

print(results)

# Plot points
fig, ax = plt.subplots()
ax.scatter(results['volatility'], results['return'])

for i in range(len(results)):
    ax.annotate([results['trigger'][i], results['window'][i]], (results['volatility'][i], results['return'][i]))

plt.show()

'''
# Print and Plot Results
print('Number of trades in period: ', int(df['trades'].tail(1)))
print('Percent of time in long position: ', sum(df['position'])/len(df['position'])*100 , '%')
print('Asset Volatility: ', vol['log_ret']*100, '%')
print('Strategy Volatility: ', vol['log_strat']*100, '%')

data_to_plot = (df[['ret', 'strat']].cumprod()-1) * 100
data_to_plot[['ret', 'strat']].plot()
df['trades'].plot()

plt.grid(visible=True)
plt.show()
'''