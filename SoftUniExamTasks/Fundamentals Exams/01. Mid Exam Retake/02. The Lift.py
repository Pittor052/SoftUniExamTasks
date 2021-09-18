people = int(input())
wagons = list(map(lambda x: int(x), input().split()))
for wagon_num in range(len(wagons)):
    if wagons[wagon_num] < 4:

        if people >= 4:
            if not wagons[wagon_num] == 0:
                num_people = 4 - wagons[wagon_num]
                people -= num_people
                wagons[wagon_num] += num_people
            else:
                people -= 4
                wagons[wagon_num] = 4
        elif not people == 0:
            num_people = people
            people -= num_people
            wagons[wagon_num] += num_people
if not wagons.count(4) == len(wagons):
    print("The lift has empty spots!")
    print(*wagons, sep=" ")
elif not people == 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons, sep=" ")
else:
    print(*wagons, sep=" ")
# 0
# 0
