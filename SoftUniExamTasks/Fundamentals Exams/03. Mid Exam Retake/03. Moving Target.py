# Shoot {index} {power}
# o Shoot the target at the index, if it exists by reducing its value by the given power (integer value).A
# target is considered shot when its value reaches 0.
# o Remove the target, if it is shot.
#  Add {index} {value}
# o Insert a target with the received value at the received index, if it exist. If not, print:
#   "Invalid placement!"
#  Strike {index} {radius}
# o Remove the target at the given index and the ones before and after it depending on the radius, if
# such exist. If any of the indices in the range is invalid print:
#   "Strike missed!" and skip this command.
targets = list(map(lambda x: int(x), input().split()))
command = input().split()

while not command[0] == "End":
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == "Shoot":
        if not 0 <= index < len(targets):
            command = input().split()
            continue
        if targets[index] - value > 0:
            targets[index] = targets[index] - value
        else:
            targets.pop(index)
    elif action == "Strike":
        if (index - value >= 0) and (index + value < len(targets)):
            del targets[index - value:index + value + 1]
        else:
            print("Strike missed!")
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    command = input().split()

print(*targets, sep="|")

# # INPUT 1
# 52 74 23 44 96 110
# Shoot 5 10
# Shoot 1 80
# Strike 2 1
# Add 22 3
# End
# # OUTPUT 1
# # Invalid placement!
# # 52|100
# # INPUT 2
# 47 55 85 78 99 20
# Shoot 1 55
# Shoot 8 15
# Strike 2 3
# Add 0 22
# Add 2 40
# Add 2 50
# End
# # OUTPUT 2
# # Strike missed!
# # 22|47|50|40|85|78|99|20
# # TEST
# 47 55 85 78 99 20
# Shoot 1 55
# Shoot 8 15
# End
