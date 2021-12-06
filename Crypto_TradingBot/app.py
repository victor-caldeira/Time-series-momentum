from binance import Client
import pandas as pd
import numpy as np
import datetime
import time

import config
from print_to_txt import print_to_txt

def get_data(ticker, interval, window):
    df = pd.DataFrame(client.get_historical_klines(ticker, interval, window))
    df = df.iloc[:,:6]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df

def trade_strategy(df, trigger, long, balance):
    df = df.copy()
    df['log_ret'] = np.log(df.Close.pct_change() + 1)
    momentum = df.log_ret.sum()
    #df.dropna(inplace = True)

    if momentum<trigger and long:
        # Sell it
        balance = balance - 10
        print_to_txt(f'{datetime.datetime.now()}, {df.Close[-1]}, {momentum}, {balance}, {long}', 'log.txt')
        '''
        print_to_txt(f'Momentum: {momentum}', 'log.txt')
        print_to_txt(f'Trade: Sell at {datetime.datetime.now()} for {df.Close[-1]}', 'log.txt')
        print_to_txt(f'Balance: {balance}', 'log.txt')
        print_to_txt('', 'log.txt')
        '''
    elif momentum>=trigger and not long:
        # Buy it
        balance = balance + 10
        print_to_txt(f'{datetime.datetime.now()}, {df.Close[-1]}, {momentum}, {balance}, {long}', 'log.txt')
        '''
        print_to_txt(f'Momentum: {momentum}', 'log.txt')
        print_to_txt(f'Trade: Buy at {datetime.datetime.now()} for {df.Close[-1]}', 'log.txt')
        print_to_txt(f'Balance: {balance}', 'log.txt')
        print_to_txt('', 'log.txt')
        '''
    else:
        print_to_txt(f'{datetime.datetime.now()}, {df.Close[-1]}, {momentum}, {balance}, {long}', 'log.txt')
        '''
        print_to_txt(f'At {datetime.datetime.now()}, Momentum: {momentum} , Long: {long}', 'log.txt')
        print_to_txt('', 'log.txt')
        '''
    
    return balance # When really running, don't need to return balance

# Initialize
print_to_txt('----------------------------------------------------', 'log.txt')
print_to_txt(f'Start running at {datetime.datetime.now()}', 'log.txt')
print_to_txt('', 'log.txt')
print_to_txt(f'Time, Price, Momentum, Balance, Long', 'log.txt')

client = Client(config.api_key, config.api_secret)
run = True

 # DELETE WHEN REALLY RUNNING
#while balance is None:
#    balance = client.get_asset_balance(asset=config.asset[:3])['free'] 
while True:
     try:
         balance = client.get_asset_balance(asset=config.asset[:3])['free']
         break
     except ValueError:
         print_to_txt("Error reading balance. Retrying...", 'log.txt')

balance = float(balance) # DELETE WHEN REALLY RUNNING

while run:
    # Uncomment WHEN REALLY RUNNING
    #while True:
    #   try:
    #        balance = client.get_asset_balance(asset=config.asset[:3])['free']
    #        break
    #   except ValueError:
    #        print_to_txt("Error reading balance. Retrying...", 'log.txt')
    
    if balance>0:
        long = True
    elif balance==0:
        long = False
    else:
        print_to_txt("Warning! Asset balance < 0", 'log.txt')
        run = False

    df = get_data(config.asset, '1d', str(config.window + 1)+' day')
    balance = trade_strategy(df, config.trigger, long, balance) # When really running, don't return balance

    time.sleep(config.trade_delay) #delay in seconds
    
