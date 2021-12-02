import numpy as np

def strategy(df, trigger, window=1):
    df = df.copy()
    df['log_ret'] = np.log(df.Close.pct_change() + 1)
    df['prior_n'] = df.log_ret.rolling(window).sum()
    df.dropna(inplace = True)

    df['position'] = [1 if i>=trigger else 0 for i in df.prior_n] # Long or neutral
    #df['position'] = [1 if i>=trigger else -1 if i<=-trigger else 0 for i in df.prior_n] # Long, short or neutral
    
    df['log_strat'] = df.position.shift(1) * df.log_ret

    df['Asset return'] = np.exp(df['log_ret'])
    df['Strategy return'] = np.exp(df['log_strat'])

    # number of trades
    df['trades'] = 0
    trades = 0
    for i in range(len(df['position']) - 1):
        if df.iloc[i]['position'] != df.iloc[i+1]['position']:
            trades += 1
        df.iloc[i+1, df.columns.get_loc('trades')] = trades

    return df