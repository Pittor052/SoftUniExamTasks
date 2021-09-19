# Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
# Remove Stop:{start_index}:{end_index} – remove the elements of the string from
# the starting index to the end index (inclusive) if both indices are valid
# Switch:{old_string}:{new_string} – if the old string is in the initial string,
# replace it with the new one. (all occurrences)

plan = input()
command = input()
output = []
while 'Travel' not in command:
    action, el1, el2 = command.split(":")

    if "Add" in action:
        el1 = int(el1)

        if 0 <= el1 < len(plan):
            plan = plan[:el1] + el2 + plan[el1:]
        output.append(plan)

    elif 'Remove' in action:
        el1 = int(el1)
        el2 = int(el2)

        if (0 <= el1 < len(plan)) and (0 <= el2 < len(plan)) and (el1 <= el2):
            plan = plan[:el1] + plan[el2 + 1:]
        output.append(plan)

    elif 'Switch' in action:

        if el1 in plan:
            plan = plan.replace(el1, el2)
        output.append(plan)

    command = input()

print(*output, sep="\n")
print(f'Ready for world tour! Planned stops: {plan}')

# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel