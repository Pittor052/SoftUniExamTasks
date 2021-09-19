import re

text = input()
regex = r'(=|\/)(?P<destination>[A-Z]{1}[A-za-z]{2,}(\1)'
result = []
points = 0
extraction = [item.group('destination') for item in re.finditer(regex, text)]

for item in extraction:
    result.append(item)
    points += len(item)

print("Destinations: ", end="")
print(*result, sep=", ")
print(f'Travel Points: {points}')
