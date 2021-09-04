sweet_bread = int(input())
points = 0
max_points = 0
winner = ""
got_max = False
print()
while not sweet_bread == 0:
    sweet_bread -= 1
    baker = input()
    command = input()
    points = 0
    while not command == "Stop":
        points += int(command)
        if points > max_points:
            max_points = points
            winner = baker
            got_max = True
        else:
            got_max = False
        command = input()
    print(f"{baker} has {points} points.")
    if got_max:
        print(f"{winner} is the new number 1!")
print(f"{winner} won competition with {max_points} points!")

# 3
# Chef Manchev
# 10
# 10
# 10
# 10
# Stop
# Natalie
# 8
# 2
# 9
# Stop
# George
# 9
# 2
# 4
# 2
# Stop