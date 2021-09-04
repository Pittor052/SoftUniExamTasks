total_eggs = int(input())
command = input()
eggs_sold = 0
while not command == "Close":
    eggs = int(input())
    if command == "Buy":
        if total_eggs < eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {total_eggs}.")
            break
        else:
            eggs_sold += eggs
            total_eggs -= eggs
    elif command == "Fill":
        total_eggs += eggs
    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")
