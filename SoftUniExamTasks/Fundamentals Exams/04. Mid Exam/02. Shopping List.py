line_stuff = input().split("!")
command = input()
while "Go Shopping!" not in command:
    command = command.split(" ")
    act = command[0]
    if act == "Urgent" and (not command[1] in line_stuff):
        line_stuff.insert(0, command[1])
    if act == "Unnecessary" and (command[1] in line_stuff):
        line_stuff.remove(command[1])
    if act == "Correct" and (command[1] in line_stuff):
        index = line_stuff.index(command[1])
        line_stuff[index] = command[2]
    if act == "Rearrange" and (command[1] in line_stuff):
        line_stuff.append(line_stuff.pop(line_stuff.index(command[1])))
    command = input()

print(", ".join([x for x in line_stuff]))
# Tomatoes!Potatoes!Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!
