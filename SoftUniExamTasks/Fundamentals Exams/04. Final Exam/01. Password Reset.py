text = input()
command = input()
output = []
while 'Done' not in command:
    if command == "TakeOdd":
        result = ''
        for i in range(1, len(text), 2):
            result += text[i]
        text = result
        output.append(text)
    elif 'Cut' in command:
        command = command.split()
        start = int(command[1])
        stop = start + int(command[2])
        text = text[:start] + text[stop:]
        output.append(text)
    elif 'Substitute' in command:
        command = command.split()
        find_this = command[1]
        replace_with = command[2]
        if find_this in text:
            text = text.replace(find_this, replace_with)
            output.append(text)
        else:
            output.append('Nothing to replace!')

    command = input()

print(*output, sep='\n')
print(f'Your password is: {text}')

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done
# # TEST
# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Done
