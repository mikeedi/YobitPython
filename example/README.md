# YoBit API usage example

* install pandas
```bash
pip3 install -r requirements.txt
```
* show orders for coin pairs


```bash
python3 orderbooks.py --pair 'eth_btc, doge_rur' --limit 5
>>>
Namespace(limit=5, pairs='eth_btc, doge_rur')
eth_btc:
      price    amount     price      amount
1  0.103593  0.043659  0.103252  107.974391
2  0.103593  0.002079  0.103190    4.793215
3  0.103770  0.174653  0.103190    1.083856
4  0.103770  6.549202  0.103189    0.342446
5  0.103800  4.355767  0.103183    0.002860

doge_rur:
    price         amount     price        amount
1  0.4121    3944.602053  0.410000     94.789311
2  0.4121   10954.708694  0.408100   4817.131268
3  0.4121   39962.003678  0.408000  88600.694672
4  0.4122    1749.339242  0.408000   9428.853991
5  0.4122  557655.277591  0.407996      8.976886
