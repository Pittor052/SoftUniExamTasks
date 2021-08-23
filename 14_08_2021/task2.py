import re

num_lines = int(input())
regex = r'^([\$|\%]){1}(?P<text>[A-Z]{1}[a-z]{2,})(\1)\:\s\[(?P<num1>\d+)(\]\|\[)(?P<num2>\d+)(\5)(?P<num3>\d+)\]\|$'
output = []
while num_lines > 0:
    text = input()
    word = [item.group('text') for item in re.finditer(regex, text)]
    num1 = [item.group('num1') for item in re.finditer(regex, text)]
    num2 = [item.group('num2') for item in re.finditer(regex, text)]
    num3 = [item.group('num3') for item in re.finditer(regex, text)]
    if word and num1 and num2 and num3:
        word, num1, num2, num3 = word[0], int(num1[0]), int(num2[0]), int(num3[0])
        result = chr(num1) + chr(num2) + chr(num3)
        output.append(f'{word}: {result}')
    else:
        output.append('Valid message not found!')
        num_lines -= 1
        continue
    num_lines -= 1
print(*output, sep='\n')