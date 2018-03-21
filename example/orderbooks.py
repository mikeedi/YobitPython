# add path to find Yobit module
import sys 
sys.path.append("../")


from Yobit.api import YoBit
import pandas as pd
import argparse

def order_table(orders, name):

    asks = orders['asks']
    asks = pd.DataFrame(asks, columns=['price', 'amount'])
    asks.index = asks.index + 1
    asks = asks.sort_index()  

    bids = orders['bids']
    bids = pd.DataFrame(bids, columns=['price', 'amount'])
    bids.index = bids.index + 1
    bids = bids.sort_index() 

    print(name + ':')

    table = pd.concat([asks, bids], axis=1)
    #set display option
    pd.set_option('display.max_rows', len(table))
    print(table)
    #reset
    pd.reset_option('display.max_rows')
    print()

def main(config):

    # initialize without API key 
    yob = YoBit()
    result = yob.depth(config.pairs, limit=config.limit)
    for name in result.keys():
        order_table(result[name], name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pairs')
    parser.add_argument('--limit', type=int, default=10)
    main(config=parser.parse_args())
