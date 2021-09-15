num_pieces = int(input())
library = {}
output = []
while True:
    while num_pieces > 0:
        piece, composer, note_key = input().split('|')
        if piece not in library:
            library[piece] = {'name': composer, 'note_key': note_key}
        num_pieces -= 1
    command = input().split('|')
    act = command[0]
    if act == 'Stop':
        break
    piece = command[1]
    if act == 'Add':
        composer, note_key = command[2], command[3]
        if piece in library:
            output.append(f"{piece} is already in the collection!")
        else:
            library[piece] = {'name': composer, 'note_key': note_key}
            output.append(f"{piece} by {composer} in {note_key} added to the collection!")
    elif act == 'Remove':
        if piece in library:
            output.append(f"Successfully removed {piece}!")
            library.pop(piece)
        else:
            output.append(f"Invalid operation! {piece} does not exist in the collection.")
    elif act == 'ChangeKey':
        new_key = command[2]
        if piece in library:
            library[piece]["note_key"] = new_key
            output.append(f"Changed the key of {piece} to {new_key}!")
        else:
            output.append(f"Invalid operation! {piece} does not exist in the collection.")
print(*output, sep='\n')
for piece, info in sorted(library.items(), key=lambda x: (x, x[1])):
    print(f'{piece} -> Composer: {info["name"]}, Key: {info["note_key"]}')
# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
