import math

command = input()
word = ""
maximum = 0
a_list = ['a', 'e', 'i', 'o', 'u', 'y', "A", "E", "I", "O", "U", "Y"]
while not command == "End of words":
    power = 0.0
    for i in range(len(command)):
        power += int(ord(command[i]))
    for j in range(0, 1):
        if command[j] in a_list:
            power *= len(command)
        else:
            power = math.floor(power / len(command))
    if power > maximum:
        word = command
        maximum = power
    command = input()

print(f"The most powerful word is {word} - {int(maximum)}")