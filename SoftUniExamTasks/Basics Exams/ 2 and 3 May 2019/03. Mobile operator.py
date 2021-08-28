duration = input()
contract = input()
internet = input()
months = int(input())
net = False
price = 0.0
discount = 3.75
if internet == "yes":
    net = True

if duration == "one":
    if contract == "Small":
        if net:
            price = (9.98 + 5.50) * months
        else:
            price = 9.98 * months
    elif contract == "Middle":
        if net:
            price = (18.99 + 4.35) * months
        else:
            price = (18.99) * months
    elif contract == "Large":
        if net:
            price = (25.98 + 4.35) * months
        else:
            price = (25.98) * months
    elif contract == "ExtraLarge":
        if net:
            price = (35.99 + 3.85) * months
        else:
            price = (35.99) * months
else:
    if contract == "Small":
        if net:
            price = ((8.58 + 5.50) * months) * 0.9625
        else:
            price = (8.58 * months) * 0.9625
    elif contract == "Middle":
        if net:
            price = ((17.09 + 4.35) * months) * 0.9625
        else:
            price = (17.09 * months) * 0.9625
    elif contract == "Large":
        if net:
            price = ((23.59 + 4.35) * months) * 0.9625
        else:
            price = (23.59 * months) * 0.9625
    elif contract == "ExtraLarge":
        if net:
            price = ((31.79 + 3.85) * months) * 0.9625
        else:
            price = (31.79 * months) * 0.9625

print(f"{price:.2f} lv.")

