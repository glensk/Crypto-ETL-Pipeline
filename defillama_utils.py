#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pandas as pd
import numpy as np
from datetime import datetime

def get_from_defillama(token,get=None,name=None):
    '''
    make api request on defillama
    examples see https://github.com/itzmestar/DeFiLlama
    '''
    # make API request
    session = requests.Session()
    url = "https://api.llama.fi/protocol/"+token
    response = session.request('GET', url, params=None, data=None, timeout=30)
    
    # check response
    if response.status_code != 200:
        print('ERROR: This request failed!')
        print('Check if the token exists:',token)
        print('Check if the url exists:',url)
        print('Request output:',response)

    return response.json()

def tvl(token):
    '''Total Value Locked in USD'''
    data_ = get_from_defillama(token) # list of dicts containing date in unixtime and tvl
    tvl_list = data_['tvl']
    token_symbol = data_['symbol']
    tvl = [d['totalLiquidityUSD'] for d in tvl_list] 
    dates_unix = [d['date'] for d in tvl_list]
    dates_readable = [np.datetime64(datetime.utcfromtimestamp(int(i)).strftime('%Y-%m-%d')) for i in dates_unix]

    # create a pandas dataframe
    data = {'date':dates_readable, 'tvl_'+token_symbol.lower():tvl}
    df = pd.DataFrame(data)
    return df
    
