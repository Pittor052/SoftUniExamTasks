h = int(input())
w = int(input())
no_paint = int(input())
litres_paint = input()
space = round((h * w * 4) * ((100 - no_paint) / 100))
while not litres_paint == "Tired!":
    space -= int(litres_paint)
    if space <= 0:
        break
    litres_paint = input()

if space < 0:
    print(f"All walls are painted and you have {abs(space)} l paint left!")
elif space == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"{space} quadratic m left.")

# 2
# 3
# 25
# 6
# 7
# 8

# 2
# 3
# 25
# 6
# 7
# 5

# 2
# 3
# 0
# 6
# 7
# 5
# 6

# 2
# 3
# 25
# 17
# Tired!