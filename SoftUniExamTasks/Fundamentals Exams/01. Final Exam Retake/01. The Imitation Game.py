text = input()

while True:
    command = input().split("|")
    act = command[0]
    if 'Decode' in act:
        print(f'The decrypted message is: {text}')
        break
    elif 'ChangeAll' in act:
        text = text.replace(command[1], command[2])
    elif 'Insert' in act:
        text = text[:int(command[1])] + command[2] + text[int(command[1]):]
    elif 'Move' in act:
        text = text[int(command[1]):] + text[:int(command[1])]
"""
zzHe
ChangeAll|z|l
Insert|2|o
Move|3
Decode

# TEST
zzHe
Decode
"""
