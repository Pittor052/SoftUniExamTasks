total_food = int(input()) * 1000
command = input()
eaten_food = 0
while not command == "Adopted":
    eaten_food += int(command)
    command = input()

if eaten_food <= total_food:
    print(f"Food is enough! Leftovers: {total_food - eaten_food} grams.")
else:
    print(f"Food is not enough. You need {eaten_food - total_food} grams more.")
