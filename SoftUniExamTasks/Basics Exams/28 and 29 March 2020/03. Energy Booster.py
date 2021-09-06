fruit = input()
size_set = input()
ordered_sets = int(input())
price = 0.0
if size_set == "small":
    price = 2.0
    if fruit == "Watermelon":
        price *= 56
    elif fruit == "Mango":
        price *= 36.66
    elif fruit == "Pineapple":
        price *= 42.10
    elif fruit == "Raspberry":
        price *= 20
if size_set == "big":
    price = 5.0
    if fruit == "Watermelon":
        price *= 28.70
    elif fruit == "Mango":
        price *= 19.60
    elif fruit == "Pineapple":
        price *= 24.80
    elif fruit == "Raspberry":
        price *= 15.20

price *= ordered_sets
if 400 <= price <= 1000:
    price *= 0.85
    print(f"{price:.2f} lv.")
elif price > 1000:
    price *= 0.5
    print(f"{price:.2f} lv.")
else:
    print(f"{price:.2f} lv.")
