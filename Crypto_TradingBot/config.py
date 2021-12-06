import os

# API key and secret
api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')

# Strategy config
asset = 'ETHUSDT'
window = 11
trigger = 0.005
trade_delay = 7200 # minimum delay in seconds between 2 trades