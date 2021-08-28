days = int(input())
hours = int(input())
total_days = days
price = 0.0
total_price = 0.0
for i in range(1, days + 1):
    for j in range(1, hours + 1):
        if (not i % 2 == 0) and (j % 2 == 0):
            price += 1.25
        elif (not i % 2 == 0) and (not j % 2 == 0):
            price += 1
        elif (i % 2 == 0) and (not j % 2 == 0):
            price += 2.50
        elif (i % 2 == 0) and (j % 2 == 0):
            price += 1
    total_price += price
    print(f"Day: {i} - {price:.2f} leva")
    price = 0.0
print(f"Total: {total_price:.2f} leva")
