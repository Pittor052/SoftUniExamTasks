group = int(input())
total = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
while not group == 0:
    group -= 1
    command = int(input())
    total += command
    if command <= 5:
        musala += command
    elif 6 <= command <= 12:
        monblan += command
    elif 13 <= command <= 25:
        kilimandjaro += command
    elif 26 <= command <= 40:
        k2 += command
    elif 41 <= command:
        everest += command

print(f"{(musala / total) * 100:.2f}%")
print(f"{(monblan / total) * 100:.2f}%")
print(f"{(kilimandjaro / total) * 100:.2f}%")
print(f"{(k2 / total) * 100:.2f}%")
print(f"{(everest / total) * 100:.2f}%")


