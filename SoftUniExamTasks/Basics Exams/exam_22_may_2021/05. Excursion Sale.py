trips_sea = int ( input () )
trips_mountain = int ( input () )
command = input ()
sold = False
profit = 0
while not command == "Stop":
    if command == "sea":
        if not trips_sea == 0:
            profit += 680
            trips_sea -= 1
        else:
            trips_sea = 0
    elif command == "mountain":
        if not trips_mountain == 0:
            profit += 499
            trips_mountain -= 1
        else:
            trips_mountain = 0
    if (trips_mountain == 0) and (trips_sea == 0):
        sold = True
        break
    command = input()

if sold:
    print("Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")
else:
    print(f"Profit: {profit} leva.")