import sys

movies = int(input())
num_movies = movies
minimum = sys.maxsize
winner = ""
loser = ""
best_rating = 0.0
average_rating = 0.0
got_max = False
got_min = False
while not movies == 0:
    movies -= 1
    name = input()
    rating = float(input())
    average_rating += rating
    points = 0
    if rating > best_rating:
        best_rating = rating
        winner = name
        got_max = True
    else:
        got_max = False
    if rating < minimum:
        minimum = rating
        loser = name
    else:
        got_min = False

print(f"{winner} is with highest rating: {best_rating}")
print(f"{loser} is with lowest rating: {minimum}")
print(f"Average rating: {average_rating / num_movies:.1f}")

# 3
# Interstellar
# 8.5
# Dangal
# 8.3
# Green Book
# 8.2