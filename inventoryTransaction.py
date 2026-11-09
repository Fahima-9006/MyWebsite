
stock = {"pen": 10, "book": 5, "bag": 2}

transactions = [
    {"type": "receive", "item": "pen", "quantity": 4},
    {"type": "sell", "item": "book", "quantity": 3},
    {"type": "sell", "item": "bag", "quantity": 5},
    {"type": "receive", "item": "ruler", "quantity": 6},
    {"type": "sell", "item": "pen", "quantity": 8}
]

accepted = 0
rejected = 0

for item in transactions:

    product = item["item"]
    quantity = item["quantity"]

    if item["type"] == "receive":

        stock[product] = stock.get(product, 0) + quantity
        accepted += 1

    elif item["type"] == "sell":

        if product in stock and stock[product] >= quantity:

            stock[product] = stock[product] - quantity
            accepted += 1

        else:
            print("Sale rejected:", product)
            rejected += 1

print("Final stock:", stock)
print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)
