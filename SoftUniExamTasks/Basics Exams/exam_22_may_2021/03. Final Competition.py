dancers = int ( input () )
points = float ( input () )
seazon = input ()
place = input ()
prize = 0.0
if place == "Bulgaria":
    prize = dancers * points
    if seazon == "summer":
        prize *= 0.95
    elif seazon == "winter":
        prize *= 0.92
if place == "Abroad":
    prize = (dancers * points) + (dancers * points * 0.5)
    if seazon == "summer":
        prize *= 0.90
    elif seazon == "winter":
        prize *= 0.85
charity = prize * 0.75
prize -= charity
print ( f"Charity - {charity:.2f}" )
print ( f"Money per dancer - {prize / dancers:.2f}" )
