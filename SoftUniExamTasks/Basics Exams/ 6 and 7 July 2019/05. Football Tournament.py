team = input()
plays = int(input())
total_plays = plays
w = 0
d = 0
l = 0
if plays == 0:
    print(f"{team} hasn't played any games during this season.")
    quit()
while plays > 0:
    command = input()
    if command == "W":
        w += 1
    elif command == "D":
        d += 1
    else:
        l += 1
    plays -= 1

print(f"{team} has won {(w * 3) + d} points during this season.")
print(f"Total stats:")
print(f"## W: {w}")
print(f"## D: {d}")
print(f"## L: {l}")
print(f"Win rate: {(w / total_plays) * 100:.2f}%")