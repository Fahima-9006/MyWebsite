
prices = {
    "rice": 75, "oil": 185, "sugar": 120,
    "milk": 95, "egg": 12, "flour": 65,
    "salt": 40, "lentil": 130, "potato": 45,
    "onion": 80, "tea": 250, "coffee": 450,
    "biscuit": 50, "soap": 70, "shampoo": 180
}

order = {}

print("How many entries do you want to provide?")
n = int(input())

for i in range(n):
    product = input("Enter the product name: ").lower()

    if product in prices:
        quantity = int(input("Enter the quantity: "))

        if quantity > 0:
            order[product] = order.get(product, 0) + quantity
            print("Product is available")

        else:
            print("Quantity should be greater than 0")

    else:
        print("Product is not available")

print("Final order:", order)

# Display the final bill
bill = {}
subtotal = 0

for item, quantity in order.items():

    unit_price = prices[item]
    total = quantity * unit_price

    bill[item] = {
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    subtotal += total

# Calculate discount
if subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

# Calculate VAT
vat = (subtotal - discount) * 0.02

# Calculate final amount
final_amount = subtotal - discount + vat

# Display the bill
print("\n================ GROCERY SHOP BILL ================")

print(f"{'Item':<12}{'Quantity':<12}{'Unit Price':<15}{'Total':<12}")

print("-" * 51)

for item, details in bill.items():

    print(f"{item:<12}{details['quantity']:<12}"
          f"{details['unit_price']:<15.2f}"
          f"{details['total']:<12.2f}")

print("-" * 51)

print(f"{'Subtotal:':<25} Tk {subtotal:.2f}")
print(f"{'Discount (5%):':<25} Tk {discount:.2f}")
print(f"{'VAT (2%):':<25} Tk {vat:.2f}")

print("-" * 51)

print(f"{'Final amount:':<25} Tk {final_amount:.2f}")

print("=" * 51)
