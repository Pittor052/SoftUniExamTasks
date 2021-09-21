line_stuff = list(map(lambda x: int(x), input().split()))
average = sum(line_stuff) / len(line_stuff)
more_than_average = []
for i in line_stuff:
    if i > average:
        more_than_average.append(i)
more_than_average.sort()
more_than_average.reverse()
for j in range(5):
    if not more_than_average:
        print("No")

    if len(more_than_average) <= 5:
        print(*more_than_average, end=" ")
        break
    print(more_than_average[j], end=" ")

