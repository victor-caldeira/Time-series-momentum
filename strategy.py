import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def strategy(df, trigger, window=1):
    df = df.copy()
    df['log_ret'] = np.log(df.Close.pct_change() + 1)
    df['prior_n'] = df.log_ret.rolling(window).sum()
    df.dropna(inplace = True)

    df['position'] = [1 if i>=trigger else 0 for i in df.prior_n]
    '''
    df['position']=0
    for i in range(len(df['position']) - 1):
        if df.iloc[i+1]['prior_n']>=trigger or (df.iloc[i+1]['prior_n']>0 and df['position'][i]==1):
            df['position'][i+1] = 1
        else:
            df['position'][i+1] = 0
    '''
    
    df['log_strat'] = df.position.shift(1) * df.log_ret

    df['ret'] = np.exp(df['log_ret'])
    df['strat'] = np.exp(df['log_strat'])

    trades = 0

    for i in range(len(df['position']) - 1):
        if df.iloc[i]['position'] != df.iloc[i+1]['position']:
            trades += 1

    print('# of trades in period: ', trades)
    print('Percent of time in long position: ', sum(df['position'])/len(df['position'])*100 , '%')
    
    df[['ret', 'strat']].cumprod().plot()
    df['position'].plot()
    df['prior_n'].plot()

    plt.grid(visible=True)
    plt.show()

    return df