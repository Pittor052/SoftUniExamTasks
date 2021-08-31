movie = input()
student = 0
standard = 0
kid = 0
total_tickets = 0
print()
while movie != "Finish":

    free_seats = int(input())
    tickets_per_movie = 0
    command = input()

    while command != "End":

        ticket_type = command
        total_tickets += 1
        tickets_per_movie += 1

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        else:
            kid += 1

        if tickets_per_movie == free_seats:
            break
        command = input()

    percent_theater_seats = tickets_per_movie / free_seats * 100
    print(f"{movie} - {percent_theater_seats:.2f}% full.")
    movie = input()

print(f"Total tickets: {total_tickets}")
percent_students = student / total_tickets * 100
print(f"{percent_students:.2f}% student tickets.")
percent_standard = standard / total_tickets * 100
print(f"{percent_standard:.2f}% standard tickets.")
percent_kid = kid / total_tickets * 100
print(f"{percent_kid:.2f}% kids tickets.")

# The Matrix
# 20
# student
# standard
# kid
# kid
# student
# student
# standard
# student
# End
# The Green Mile
# 17
# student
# standard
# standard
# student
# standard
# student
# End
# Amadeus
# 3
# standard
# standard
# standard
# End
# How High
# 1
# student
# Finish
