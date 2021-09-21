processed_people = int(input()) + int(input()) + int(input())
people_left = int(input())
hours = 0

while people_left > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    people_left -= processed_people

print(f"Time needed: {hours}h.")