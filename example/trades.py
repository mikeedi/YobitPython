# add path to find Yobit module
import sys 
sys.path.append("../")


from Yobit.api import YoBit
import time
import pandas as pd
import argparse


def trade_table(books, name):
    print(name + ':')

    for order in books:
        # slice remove day of the week and year
        timestamp = time.ctime(int(order['timestamp']))[4:-5]
        amount = order['amount']
        price = order['price']
        bORs = order['type']
        if bORs == 'bid':
            print("\033[32m" + "{} {} {} {}".format(timestamp, 'BUY', float(price), float(amount)))
        else:
            print("\033[31m" + "{} {} {} {}".format(timestamp, 'SELL', float(price), float(amount)))
    print("\033[39m")       

def main(config):
    # initialize without API key 
    yob = YoBit()
    result = yob.trades(config.pairs, limit=config.limit)
    for name in result.keys():
        trade_table(result[name], name)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pairs', type=str)
    parser.add_argument('--limit', type=int, default=10)
    main(config=parser.parse_args())
