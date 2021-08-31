budget = float(input())
crew = int(input())
price_clothes = float(input()) * crew

if crew > 150:
    price_clothes *= 0.9

expenses = float((budget * 0.1) + price_clothes)

if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(expenses - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")
