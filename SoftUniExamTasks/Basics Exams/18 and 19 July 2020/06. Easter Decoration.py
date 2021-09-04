clients = int(input())
total_client = clients
items = 0
total_sum = 0.0
suma = 0.0
print()
while clients > 0:
    clients -= 1
    command = input()
    suma = 0
    items = 0
    while not command == "Finish":
        items += 1
        if command == "basket":
            suma += 1.5
        elif command == "wreath":
            suma += 3.8
        elif command == "chocolate bunny":
            suma += 7
        command = input()
    if items % 2 == 0:
        suma *= 0.8
    print(f"You purchased {items} items for {suma:.2f} leva.")
    total_sum += suma
print(f"Average bill per client is: {total_sum  / total_client:.2f} leva.")
