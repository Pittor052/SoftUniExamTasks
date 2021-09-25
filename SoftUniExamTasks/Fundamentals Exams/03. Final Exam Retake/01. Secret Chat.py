text = input()
command = input()
output = []

while 'Reveal' not in command:

    command = command.split(':|:')
    action = command[0]

    if action == 'InsertSpace':
        # InsertSpace:|:{index}
        # oInserts a single empty space at the given index. The given index will always be valid.
        index = int(command[1])
        text = text[:index] + " " + text[index:]
        output.append(text)

    elif action == 'ChangeAll':
        # ChangeAll:|:{substring}:|:{replacement}
        # oChanges all occurrences of the given substring with the replacement text.
        change_this = command[1]
        with_this = command[2]
        text = text.replace(change_this, with_this)
        output.append(text)

    elif action == 'Reverse':
        # Reverse:|:{substring}
        # oIf the message contains the given substring, cut it out, reverse it and add it AT THE END of the message.
        # oIf not, print "error".
        # oThis operation should replace only the first occurrence of the given substring if
        # there are more than one such occurrences.
        substring = command[1]

        if substring in text:
            new = substring[::-1]
            text = text.replace(substring, '', 1)  # remove the substring
            text = text + new  # add the reversed substring AT THE END
            output.append(text)

        else:
            output.append("error")

    command = input()

print(*output, sep='\n')
print(f'You have a new text message: {text}')

# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal

# # TEST
# heVVodar!gniV
# InsertSpace:|:5
# Reverse:|:!gnil
# Reveal
