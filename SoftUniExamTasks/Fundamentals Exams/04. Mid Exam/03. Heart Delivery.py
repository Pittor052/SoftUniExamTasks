targets = list(map(lambda x: int(x), input().split("@")))
command = input().split()
count = 0
while not command[0] == "Love!":
    jump = int(command[1])
    count += jump
    if count >= len(targets):
        count = 0

    if targets[count] == 0:
        print(f"Place {count} already had Valentine's day.")
        command = input().split()
        continue

    targets[count] -= 2

    if targets[count] == 0:
        print(f"Place {count} has Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {count}.")
if len(targets) == targets.count(0):
    print(f"Mission was successful.")

else:
    print(f"Cupid has failed {len(targets) - (targets.count(0))} places.")

# 10@10@10@2
# Jump 1
# Jump 2
# Love!

# 2@4@2
# Jump 2
# Jump 2
# Jump 8
# Jump 3
# Jump 1
# Love!
# # TEST

