line_stuff = list(map(lambda x: int(x), input().split()))
command = input()
while "end" not in command:
    command = command.split(" ")
    act = command[0]
    if act == "swap":
        line_stuff[int(command[1])], line_stuff[int(command[2])] = line_stuff[int(command[2])], \
                                                                   line_stuff[int(command[1])]
    if act == "multiply":
        line_stuff[int(command[1])] = line_stuff[int(command[1])] * line_stuff[int(command[2])]
    if act == "decrease":
        for number in range(len(line_stuff)):
            line_stuff[number] -= 1
    command = input()

print(", ".join([str(x) for x in line_stuff]))
