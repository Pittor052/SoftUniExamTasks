import math
import re

text = input()
regex = r'([\||\#]){1}(?P<item>[A-Za-z]+[\sA-Za-z]*)(\1)(?P<date>\d{2}\/\d{2}\/\d{2})(\1)(?P<cal>[0-9]+)(\1)'

item = [item.group('item') for item in re.finditer(regex, text)]
date = [item.group('date') for item in re.finditer(regex, text)]
cal = [int(item.group('cal')) for item in re.finditer(regex, text)]

print(f'You have food to last you for: {int(sum(cal)/2000)} days!')

for stats in range(len(item)):
    print(f'Item: {item[stats]}, Best before: {date[stats]}, Nutrition: {cal[stats]}')
