coffee = input()
sugar = input()
orders = float(input())
price = 0.0
total_price = 0.0
if coffee == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif coffee == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.6
elif coffee == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7
total_price = price * orders
if sugar == "Without":
    total_price = (price * orders) * 0.65
if coffee == "Espresso" and orders >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.8

print(f"You bought {int(orders)} cups of {coffee} for {total_price:.2f} lv.")
