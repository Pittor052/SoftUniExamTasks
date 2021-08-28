chicken = int(input()) * 10.35
fish = int(input()) * 12.40
veg = int(input()) * 8.15
total = chicken + fish + veg
total += (total * 0.20)
print(f"Total: {total + 2.50:.2f}")