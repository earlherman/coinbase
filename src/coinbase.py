#!/usr/bin/env python

import cbpro
myClient    = cbpro.PublicClient()
ticprice    = myClient.get_product_ticker(product_id='XRP-USD')
print(ticprice["bid"])
