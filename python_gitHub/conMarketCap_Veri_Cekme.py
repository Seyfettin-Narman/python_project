from requests import Request, Session
from requests.exceptions import ConnectionError,Timeout,TooManyRedirects
import json
url='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters={'start':'1',
            'limit':'5000',
            'convert':'USD'
            }
basliklar={'Accepts':'application/json',
           'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
           }
oturum=Session()
oturum.headers.update(basliklar)
try:
    cevap= oturum.get(url,params=parameters)
    veri=json.loads(cevap.text)
    print(veri)
except(ConnectionError,Timeout,TooManyRedirects) as f:
    print(f)