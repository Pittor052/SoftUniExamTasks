number = int(input())
total_number = number
p1 = 0
p2 = 0
p3 = 0
while not total_number == 0:
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1
    total_number -= 1
print(f"{(p1 / number) * 100:.2f}%")
print(f"{(p2 / number) * 100:.2f}%")
print(f"{(p3 / number) * 100:.2f}%")