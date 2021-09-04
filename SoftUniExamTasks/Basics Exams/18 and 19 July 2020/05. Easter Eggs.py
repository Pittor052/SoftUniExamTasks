eggs = int(input())
red = 0
green = 0
blue = 0
orange = 0
while eggs > 0:
    command = input()
    if command == "red":
        red += 1
        eggs -= 1
    elif command == "green":
        green += 1
        eggs -= 1
    elif command == "blue":
        blue += 1
        eggs -= 1
    elif command == "orange":
        orange += 1
        eggs -= 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
if (red >= orange) and (red >= blue) and (red >= green):
    print(f"Max eggs: {red} -> red")
elif (orange >= red) and (orange >= blue) and (orange >= green):
    print(f"Max eggs: {orange} -> orange")
elif (blue >= red) and (blue >= orange) and (blue >= green):
    print(f"Max eggs: {blue} -> blue")
else:
    print(f"Max eggs: {green} -> green")
