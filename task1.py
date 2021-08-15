text = input()
output = []
while True:
    command = input().split()
    if "Finish" in command[0]:
        break
    act = command[0]

    if act == "Replace":
        find_this = command[1]
        replace_with = command[2]
        text = text.replace(find_this, replace_with)
        output.append(text)
    elif act == 'Cut':
        start = int(command[1])
        stop = int(command[2])
        if 0 < start < len(text) and 0 < stop < len(text) and start <= stop:
            text = text[:start] + text[stop + 1:]
            output.append(text)
        else:
            output.append("Invalid indices!")
    elif act == 'Make':
        case = command[1]
        if case == 'Upper':
            text = text.upper()
            output.append(text)
        else:
            text = text.lower()
            output.append(text)
    elif act == 'Check':
        if command[1] in text:
            output.append(f"Message contains {command[1]}")
        else:
            output.append(f"Message doesn't contain {command[1]}")
    elif act == 'Sum':
        start = int(command[1])
        stop = int(command[2])
        if 0 < start < len(text) and 0 < stop < len(text) and start <= stop:
            result = 0
            for char in range(start, stop + 1):
                result += ord(text[char])
            output.append(result)
        else:
            output.append("Invalid indices!")
print(*output, sep='\n')

# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish
