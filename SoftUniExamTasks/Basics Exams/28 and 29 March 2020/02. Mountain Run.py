import math

record = float(input())
distance = float(input())
climbing = float(input())
minutes = distance * climbing
slowing = math.floor((distance / 50)) * 30
total_seconds = minutes + slowing
if record <= total_seconds:
    print(f"No! He was {abs(record - total_seconds):.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_seconds:.2f} seconds.")
