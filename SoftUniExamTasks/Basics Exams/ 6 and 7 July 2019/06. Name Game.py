name = input()
match = 0
winner = ""
maximum = 0
while not name == "Stop":
    for i in range(len(name)):
        command = int(input())
        if int(ord(name[i])) == command:
            match += 10
        else:
            match += 2
    if match >= maximum:
        winner = name
        maximum = match
        match = 0
    name = input()

print(f"The winner is {winner} with {maximum} points!")

# Ivan
# 73
# 20
# 98
# 110
# Ivo
# 80
# 65
# 87
# Stop

# efgh
# 101
# 102
# 103
# 104
# abcd
# 97
# 98
# 99
# 100
# Stop

# efgh
# 1
# 1
# 1
# 1
# abcd
# 9
# 9
# 9
# 10
# Stop


