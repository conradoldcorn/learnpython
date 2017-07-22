stock_dict = {'hay': 3, 'food': 1, 'banana_chips': 4}

# Iterate through the stock, if the value of the item is 1 or less, print 'Order more ITEM'
in_stock = []

for key, val in stock_dict.items():
        if val <= 1:
            print("Order more: {}".format(key))

        else:

            in_stock.append(key)

print("You don't need to order {}".format(in_stock.))



#for item in stock_dict:
    # print(stock_dict.items())
    #if stock_dict.items():
        #print("Order more {}".format(stock_dict.items()))