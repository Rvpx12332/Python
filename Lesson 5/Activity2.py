sell_price = int(input("Enter the selling price:"))
cost_price = int(input("Enter the cost price:"))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print("Your profit is:", profit)
else:
    loss = cost_price - sell_price
    print("Your loss is", loss)