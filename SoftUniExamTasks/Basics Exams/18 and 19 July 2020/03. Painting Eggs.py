size_eggs = input()
color = input()
num = int(input())
price = 0
total_sum = 0.0
if size_eggs == "Large":
    if color == "Red":
        price = 16
    elif color == "Green":
        price = 12
    else:
        price = 9
elif size_eggs == "Medium":
    if color == "Red":
        price = 13
    elif color == "Green":
        price = 9
    else:
        price = 7
elif size_eggs == "Small":
    if color == "Red":
        price = 9
    elif color == "Green":
        price = 8
    else:
        price = 5

print(f"{(num * price) - (num * price * 0.35):.2f} leva.")
