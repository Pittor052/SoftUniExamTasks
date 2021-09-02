a1 = int(input())
a2 = int(input())
n = int(input())
for p in range(a1, ord(chr(a2 - 1)) + 1):
    for i in range(1, (n - 1) + 1):
        for j in range(1, (int((n / 2) - 1)) + 1):
            if (p % 2 != 0) and (((i + j + p) % 2) != 0):
                print(f"{chr(p)}-{i}{j}{p}")
