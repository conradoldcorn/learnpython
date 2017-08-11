# Iterate through the stock, if the value of the item is 1 or less, print 'Order more ITEM'
import random

stock_dict = {'hay': random.randint(0,10), 'food': random.randint(0,10), 'banana_chips': random.randint(0,10)}

#random.choice(stock_dict.items())
print(stock_dict)

in_stock = []
out_stock = []

for key, val in stock_dict.items():
        if val <= 1:
            out_stock.append(key)

        else:

            in_stock.append(key)

formatted_out_stock = ', '.join(out_stock)
formatted_in_stock = ', '.join(in_stock)

#if formatted_out_stock.items(<= 1):
print("Order more: {}".format(formatted_out_stock))
print("You don't need to order {}".format(formatted_in_stock))
