sold_games = int(input())
total_games = sold_games
h = 0
f = 0
ov = 0
other = 0
a_list = ["Hearthstone", "Fornite", "Overwatch"]
while sold_games > 0:
    command = input()
    if command in a_list:
        if command == "Hearthstone":
            h += 1
        elif command == "Fornite":
            f += 1
        elif command == "Overwatch":
            ov += 1
    else:
        other += 1
    sold_games -= 1

print(f"Hearthstone - {(h / total_games) * 100:.2f}%")
print(f"Fornite - {(f / total_games) * 100:.2f}%")
print(f"Overwatch - {(ov / total_games) * 100:.2f}%")
print(f"Others - {(other / total_games) * 100:.2f}%")
