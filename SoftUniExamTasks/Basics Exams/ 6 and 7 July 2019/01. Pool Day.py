import math

people = int(input())
tax_entry = float(input()) * people
price_chair = float(input())
price_umbrella = float(input())
chairs = math.ceil(people * 0.75) * price_chair
umbrella = math.ceil(people / 2) * price_umbrella
print(f"{tax_entry + chairs + umbrella:.2f} lv.")

