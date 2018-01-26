"""
Yobit API implementation

"""

import requests
import json
import hmac
import time
import hashlib
from urllib.parse import urlencode
from urllib.request import urlopen, Request




class YoBit():
    def __init__(self, key=None, secret=None):
        self.key = key
        self.secret = secret
        self.url_trade = 'https://yobit.net/tapi/'
        self.url_public = 'https://yobit.net/api/3/'

    def getInfo(self):
        """
        desription
        """
        params = {'method' : 'getInfo',
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if response['success'] == 1:
            return response['return']
        else:
            return response['error']

    def Trade(self, pair, bORs, rate, amount):
        """
        desription
        """
        params = {
                'method' : 'Trade',
                'pair' : pair,
                'type' : bORs,
                'rate' : rate,
                'amount' : amount,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if response['success'] == 1:
            return response['return']
        else:
            return response['error']

    def ActiveOrders(self, pair):
        """
        type(pair) :: string

        >>> pair = 'ltc_btc'
        """
        params = {
                'method' : 'ActiveOrders',
                'pair' : pair,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error']
        else:
            return 'You dont have orders for this pair'    

    def OrderInfo(self, order_id):
        """
        type(order_id) :: string or int
        """
        params = {
                'method' : 'OrderInfo',
                'order_id' : order_id,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error']

    def CancelOrder(self, order_id):
        """
        type(order_id) :: string or int
        """
        params = {
                'method' : 'CancelOrder',
                'order_id' : order_id,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error']

    def TradeHistory(self, pair, start=0, count=1000, from_id=0,  
                            end_id=None, order='DESC', since=0, end=None):
        """
        
        """
        params = {
                'method' : 'TradeHistory',
                'pair' : pair,
                'start' : start,
                'count' : count,
                'from_id' : from_id,
                'end_id' : end_id,
                'order' : order,
                'since' : since,
                'end' : end,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error']

    def GetDepositAddress(self, coinName, need_new=0):
        """
        """
        params = {
                'method' : 'GetDepositAddress',
                'coinName' : coinName,
                'need_new' : need_new,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error'] 

    def WithdrawCoinsToAddress(self, coinName, amount, address):
        """
        """
        params = {
                'method' : 'WithdrawCoinsToAddress',
                'coinName' : coinName,
                'amount' : amount,
                'address' : address,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response        

    def CreateYobicode(self, currency, amount):
        """
        """
        params = {
                'method' : 'CreateYobicode',
                'currency' : currency,
                'amount' : amount,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response

    def RedeemYobicode(self, coupon):
        """
        """
        params = {
                'method' : 'RedeemCoupon',
                'coupon' : coupon,
                'nonce' : str(int(time.time()))}
        body = urlencode(params).encode()
        signature = hmac.new(
                        self.secret.encode(),
                        body,  
                        hashlib.sha512).hexdigest()
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Sign' : signature,
            'Key' : self.key,
        }
        req = requests.post(self.url_trade, body, headers=headers)
        response =  json.loads(req.text)
        if 'return' in response.keys():
            return response['return']
        elif 'error' in response.keys():
            return response['error']             


    """Method without key and secret"""
    def info(self):
        """

        """
        url = self.url_public + 'info'
        req = requests.get(url)
        return json.loads(req.text)

    def ticker(self, pairs=None):
        """
        statistic for each pair
        if pairs = ['ltc_btc', 'bch_btc'] 
        then url looks like https://yobit.net/api/3/ticker/ltc_btc-waves_btc
        """
        url = self.url_public + 'ticker/'
        for i in range(len(pairs)):
            url += pairs[i]
            if i != len(pairs) - 1:
                url += '-' 

        req = requests.get(url)
        return json.loads(req.text)

    def depth(self, limit=10, pairs=[]):
        """
        description
        """
        url = self.url_public + 'depth/'
        for i in range(len(pairs)):
            url += pairs[i]
            if i != len(pairs) - 1:
                url += '-'

        req = requests.get(url, params={'limit' : limit})
        return json.loads(req.text)


    def trades(self, limit=10, pairs=[]):
        """
        description
        """
        url = self.url_public + 'trades/'
        for i in range(len(pairs)):
            url += pairs[i]
            if i != len(pairs) - 1:
                url += '-'

        req = requests.get(url, params={'limit' : limit})
        return json.loads(req.text)
