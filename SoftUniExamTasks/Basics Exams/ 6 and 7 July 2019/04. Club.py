target = float(input())
cocktail = input()
income = 0.0
target_reached = False
while not cocktail == "Party!":
    command = int(input())
    price = len(cocktail) * command
    if not price % 2 == 0:
        price *= 0.75
    income += price
    if income >= target:
        break
    cocktail = input()
if income >= target:
    print("Target acquired.")
    print(f"Club income - {income:.2f} leva.")
else:
    print(f"We need {target - income:.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")
