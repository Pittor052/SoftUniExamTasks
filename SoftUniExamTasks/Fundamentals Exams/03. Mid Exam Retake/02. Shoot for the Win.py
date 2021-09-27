targets = list(map(lambda x: int(x), input().split()))
shot_targets = []
while True:
    command = input()

    if command == 'End':
        print(f"Shot targets: {targets.count(-1)} -> ", end="")
        print(*targets, sep=" ")
        break

    index = int(command)

    if not 0 <= index <= len(targets) - 1:
        continue

    test = targets[index]
    targets[index] = -1
    shot_targets.append(index)
    for i in range(len(targets)):

        if i in shot_targets:
            continue

        if test < targets[i]:
            targets[i] -= test
            continue

        if test >= targets[i] and not index == i:
            targets[i] += test
