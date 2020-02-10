#!/usr/bin/env python

import cbpro, time
myClient    = cbpro.PublicClient()

maxprice    = 0
minprice    = 0
iniprice    = 0
while True:
    ticprice    = myClient.get_product_ticker(product_id='XRP-USD')["price"]
    if maxprice == 0 and minprice == 0:
        iniprice = maxprice = minprice = ticprice
        print("Initial Price set: ${}".format(iniprice))
    elif ticprice > maxprice:
        maxprice = ticprice
        print("Max Price increase: ${}".format(maxprice))
    elif ticprice < minprice:
        minprice = ticprice
        print("Min Price decrease: ${}".format(minprice))

    time.sleep(1)
