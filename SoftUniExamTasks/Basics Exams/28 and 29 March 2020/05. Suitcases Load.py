capacity = float(input())
c = capacity
suitcase = 0
load = 0.0
more_load = 0.0
command = input()
count = 1
stop = False
while not command == "End":
    load = float(command)
    if load > c:
        stop = True
        print("No more space!")
        break
    if load == c:
        suitcase += 1
        break
    elif count == 3:
        more_load = (float(command) / 10)
        count = 0
    c -= (float(command) + more_load)
    more_load = 0.0
    suitcase += 1
    count += 1
    command = input()

if not stop:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcase} suitcases loaded.")
