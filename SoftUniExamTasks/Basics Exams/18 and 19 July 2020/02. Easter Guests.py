import math

guests = int(input())
budget = int(input())
price_sweet_bread = math.ceil(guests / 3) * 4
price_eggs = (guests * 2) * 0.45
total_sum = price_eggs + price_sweet_bread
if total_sum <= budget:
    print(f"Lyubo bought {int(price_sweet_bread / 4)} Easter bread and {int(price_eggs / 0.45)} eggs.")
    print(f"He has {abs(total_sum - budget):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(total_sum - budget):.2f} lv. more.")

