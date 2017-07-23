stock_dict = {'hay': 3, 'food': 1, 'banana_chips': 0}

# Iterate through the stock, if the value of the item is 1 or less, print 'Order more ITEM'
in_stock = []
out_stock = []


for key, val in stock_dict.items():
        if val <= 1:
            out_stock.append(key)

        else:

            in_stock.append(key)

formatted_out_stock = ', '.join(out_stock)
formatted_in_stock = ', '.join(in_stock)

print("Order more: {}".format(formatted_out_stock))
print("You don't need to order {}".format(formatted_in_stock))