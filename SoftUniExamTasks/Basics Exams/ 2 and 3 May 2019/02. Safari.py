budget = float(input())
fuel = (float(input()) * 2.10) + 100
day = input()
if day == "Saturday":
    fuel *= 0.90
else:
    fuel *= 0.80
if fuel <= budget:
    print(f"Safari time! Money left: {budget - fuel:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(budget - fuel):.2f} lv.")
