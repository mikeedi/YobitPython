import sys 
sys.path.append("../")

import requests
import json
import hmac
import time
import hashlib
from urllib.parse import urlencode
from urllib.request import urlopen, Request

from Yobit.api import YoBit

class WEX(YoBit):
    def __init__(self, key=None, secret=None):
        self.key = key
        self.secret = secret
        self.url_trade = 'https://wex.nz/tapi/'
        self.url_public = 'https://wex.nz/api/3/'