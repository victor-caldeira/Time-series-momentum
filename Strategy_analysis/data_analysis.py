import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from strategy import strategy

# Import data
df = yf.download('ETH-USD', start = '2020-12-3', interval = '1d') # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

# Run Strategy with different Triggers and windows
results = pd.DataFrame(columns = ['trigger', 'window', 'return', 'volatility'])
for trigger in np.linspace(0, 0.01, 5):
    for window in np.linspace(8, 13, 6, dtype=int):
        df_i = strategy(df, trigger, window)
        #dfs.append(df_i)
        
        vol = df_i[['log_strat']].std()*len(df)**.5 * 100
        strat_ret = (df_i[['Strategy return']].prod() - 1) * 100
        
        results.loc[len(results)] = [round(trigger,4) , window, float(strat_ret), float(vol)]

    print('Trigger ', round(trigger,4), ' calculated')

print(results)

# Plot points
fig, ax = plt.subplots()
ax.scatter(results['volatility'], results['return'])

for i in range(len(results)):
    ax.annotate([results['trigger'][i], results['window'][i]], (results['volatility'][i], results['return'][i]))

plt.title('Momentum Strategy ETH-USD (Return on period: 728.42%, vol: 108,4%)\n[Trigger, Window(days)]')
plt.xlabel('Volatility (%)')
plt.ylabel('Return (%)')

plt.show()
