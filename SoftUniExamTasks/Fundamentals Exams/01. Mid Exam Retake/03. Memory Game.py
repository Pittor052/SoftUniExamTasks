line_input = list(input().split())
moves = 0
gg = False
while True:
    command_input = input()
    if len(line_input) == 0:
        gg = True
        break
    elif command_input == "end":
        break
    index = (len(line_input) // 2)
    moves += 1
    command = list((int(x) for x in command_input.split()))

    if (-1 < command[0] < len(line_input)) and (-1 < command[1] < len(line_input)):
        if line_input[command[0]] == line_input[command[1]]:
            print(f"Congrats! You have found matching elements - {line_input[command[0]]}!")
            line_input = list(filter(lambda a: a != line_input[command[0]] and line_input[command[1]], line_input))
        else:
            print("Try again!")
    else:
        print("Invalid input! Adding additional elements to the board")
        line_input.insert(index, f"{-1 * moves}a")
        line_input.insert(index, f"{-1 * moves}a")
if gg:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*line_input, sep=" ")

# 1 1 2 2 3 3 4 4 5 5
# 1 0
# -1 0
# 1 0
# 1 0
# 1 0
# end
# # TEST
# 1 1 2 2 3 3 4 4 5 5
# -1 0
# end
#
# a 2 4 a 2 4
# 0 3
# 0 2
# 0 1
# 0 1
# end