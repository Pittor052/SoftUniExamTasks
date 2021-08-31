rent = int(input())
statues = rent - (rent * 30) / 100
catering = statues - (statues * 15) / 100
sound = catering / 2
print(f"{statues + catering + sound + rent:.2f}")
