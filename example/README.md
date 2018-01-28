# YoBit API usage example

* install pandas
```bash
pip3 install -r requirements.txt
```
* show orders for coin pairs


```bash
python3 orderbooks.py --pair 'eth_btc, doge_rur' --limit 5
>>>Namespace(limit=5, pairs='eth_btc, doge_rur')
eth_btc:
      price    amount     price      amount
1  0.103593  0.043659  0.103252  107.974391
2  0.103593  0.002079  0.103190    4.793215
....

doge_rur:
    price         amount     price        amount
1  0.4121    3944.602053  0.410000     94.789311
2  0.4121   10954.708694  0.408100   4817.131268
....
```
  * show last books (with color in terminal)
```bash
python trades.py --pair 'doge_rur, eth_btc, trx_rur' --limit 5
>>>Namespace(limit=5, pairs='doge_rur, eth_btc, trx_rur')
doge_rur:
Jan 28 19:46:38 BUY 0.41099995 213.36856745
Jan 28 19:46:15 BUY 0.41099996 229.95398373
....

eth_btc:
Jan 28 19:46:31 SELL 0.10267722 0.00187976
Jan 28 19:45:58 SELL 0.10319 0.14854089
....

trx_rur:
Jan 28 19:46:31 SELL 3.72628458 43.69501218
Jan 28 19:46:29 BUY 3.72676241 5.92427865
....
```

