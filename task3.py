fighters = {}
output = []
while True:
    command = input()
    if 'Results' in command:
        output.append(f'People count: {len(fighters)}')
        break

    elif 'Add' in command:  # "Add:{personName}:{health}:{energy}"
        act, name, hp, en = command.split(':')
        if name not in fighters:
            fighters[name] = {'hp': int(hp), 'en': int(en)}
        else:
            fighters[name]['hp'] += int(hp)
    elif 'Attack' in command:  # "Attack:{attackerName}:{defenderName}:{damage}"
        act, attackerName, defenderName, damage = command.split(':')
        damage = int(damage)
        if (attackerName in fighters) and (defenderName in fighters):
            fighters[defenderName]['hp'] -= damage
            fighters[attackerName]['en'] -= 1
            if fighters[defenderName]['hp'] <= 0:
                fighters.pop(defenderName)
                output.append(f'{defenderName} was disqualified!')

            if fighters[attackerName]['en'] <= 0:
                fighters.pop(attackerName)
                output.append(f'{attackerName} was disqualified!')
    elif 'Delete' in command:  # "Delete:{username}"
        name = command.split(':')[1]
        if name == 'All':
            fighters.clear()
        elif name in fighters:
            fighters.pop(name)

print(*output, sep='\n')
if not len(fighters) == 0:
    for name, stats in sorted(fighters.items(), key=lambda x: (-x[1]['hp'], x)):
        print(f"{name} - {stats['hp']} - {stats['en']}")

# Add:Mark:1000:5
# Delete:ALL
# Results