#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pandas as pd

def get_from_glassnode(token,get=None,name=None):
    ''' get a particular metric from glassnode {price_usd_close,marketcap_usd, ...}'''

    # your glassnode API key
    API_KEY = '212yOGwljnmHZtlO9zfOOoTav2O'

    # make API request
    url = 'https://api.glassnode.com/v1/metrics/'+get
    response = requests.get(url,params={'a': token, 'api_key': API_KEY})
    if response.status_code != 200:
        print('ERROR: This request failed!')
        print('Check if the token exists:',token)
        print('Check if the url exists:',url)
        print('Request output:',response)

    # format the pandas dataframe
    df = pd.read_json(response.text, convert_dates=['t'])
    out = df.rename(columns={"v": name+"_"+token.lower(),"t":"date"})
    return out

def price(token):
    '''Price in USD'''
    return get_from_glassnode(token,get='market/price_usd_close',name='price')

def sopr(token):
    '''SOPR'''
    return get_from_glassnode(token,get='indicators/sopr',name='sopr')

def marketcap(token):
    '''Marketcap'''
    return get_from_glassnode(token,get='market/marketcap_usd',name='mc')

def tvl(token):
    '''Total Value locked'''
    return get_from_glassnode(token,get='defi/total_value_locked',name='tvl')


