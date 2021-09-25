import re

text = input()
regex = r'([@|#]{1})([A-Za-z]{3,})(\1){2}([A-Za-z]{3,})(\1)'
result = []

words = [item.group(2, 4) for item in re.finditer(regex, text)]

if len(words) == 0:
    print('No word pairs found!')
else:
    print(f'{len(words)} word pairs found!')
for pair in words:
    if pair[0][::-1] == pair[1]:
        result.append(f'{pair[0]} <=> {pair[1]}')
if len(result) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(*result, sep=", ")



