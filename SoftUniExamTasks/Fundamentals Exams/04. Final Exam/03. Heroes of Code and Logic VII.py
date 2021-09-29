#  {hero name} {HP} {MP}
num_heroes = int(input())
heroes = {}
output = []

while num_heroes > 0:
    name, mp, hp = input().split()
    if name not in heroes:
        heroes[name] = {'hp': int(mp), 'mp': int(hp)}
    num_heroes -= 1

while True:
    command = input().split(' - ')
    action = command[0]
    if action == "End":
        break
    elif 'CastSpell' in action:  # CastSpell – {hero name} – {MP needed} – {spell name}
        name, mp, spell = command[1], int(command[2]), command[3]
        if heroes[name]['mp'] >= mp:
            heroes[name]['mp'] -= mp
            output.append(f"{name} has successfully cast {spell} and now has {heroes[name]['mp']} MP!")
        else:
            output.append(f"{name} does not have enough MP to cast {spell}!")
    elif 'TakeDamage' in action:  # TakeDamage – {hero name} – {damage} – {attacker}
        name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[name]['hp'] -= damage
        if heroes[name]['hp'] > 0:
            output.append(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")
        else:
            output.append(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
    elif 'Recharge' in action:  # Recharge – {hero name} – {amount}
        name, amount = command[1], int(command[2])

        if (heroes[name]['mp'] + amount) > 200:
            amount = 200 - heroes[name]['mp']

        heroes[name]['mp'] += amount
        output.append(f"{name} recharged for {amount} MP!")
    elif 'Heal' in action:  # Heal – {hero name} – {amount}
        name, amount = command[1], int(command[2])

        if (heroes[name]['hp'] + amount) > 100:
            amount = 100 - heroes[name]['hp']

        heroes[name]['hp'] += amount
        output.append(f"{name} healed for {abs(amount)} HP!")

print(*output, sep='\n')
for name, stats in sorted(heroes.items(), key=lambda x: (-x[1]['hp'], x[0])):
    print(name)
    print(f'  HP: {heroes[name]["hp"]}')
    print(f'  MP: {heroes[name]["mp"]}')
