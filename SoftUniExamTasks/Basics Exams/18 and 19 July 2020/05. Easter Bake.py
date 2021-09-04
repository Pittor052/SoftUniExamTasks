import math

sweet_bread = int(input())
total_sugar = 0
total_flour = 0
max_flour = 0
max_sugar = 0
while sweet_bread > 0:
    sugar = int(input())
    flour = int(input())
    total_sugar += sugar
    total_flour += flour
    sweet_bread -= 1
    if max_sugar <= sugar:
        max_sugar = sugar
    if max_flour <= flour:
        max_flour = flour

packets_sugar = math.ceil(total_sugar / 950)
packets_flour = math.ceil(total_flour / 750)
print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")