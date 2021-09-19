import re

regex = r'([A-Z]\w+): ([A-Z]*\w+)[\-\ \ ]*(\d+[\.\d+]*)*'
num_plants = int(input())
plants = {}

while num_plants > 0:
    plant, rating = input().split('<->')

    if plant not in plants:
        plants[plant] = [int(rating)]

    else:
        plants[plant] = [int(rating)]

    num_plants -= 1

command = input()

while 'Exhibition' not in command:

    name = [item.group(2) for item in re.finditer(regex, command)]

    if name not in plants:
        print('error')
        command = input()
        continue

    act = [item.group(1) for item in re.finditer(regex, command)]
    rating = [item.group(3) for item in re.finditer(regex, command)]
    act, name, rating = str(act[0]), str(name[0]), str(rating[0])

    if act == 'Rate':
        plants[name].append(int(rating))

    elif act == 'Update':
        plants[name].pop(0)
        plants[name].insert(0, int(rating))

    elif act == 'Reset':
        rarity = plants[name].pop(0)
        plants[name].clear()
        plants[name].append(rarity)

    command = input()

print('Plants for the exhibition:')

for name, stats in plants.items():

    if not len(stats) == 1:
        r = stats.pop(0)
        plants[name] = [sum(stats) / len(stats)]
        plants[name].insert(0, r)

    else:
        plants[name].append(0)

for name, values in sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f'- {name}; Rarity: {values[0]}; Rating: {values[1]:.2f}')

# # INPUT 0
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
# # OUTPUT 0
# Plants for the exhibition:
# - Woodii; Rarity: 5; Rating: 7.50
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Welwitschia; Rarity: 2; Rating: 7.00

# # TEST
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: asd - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
