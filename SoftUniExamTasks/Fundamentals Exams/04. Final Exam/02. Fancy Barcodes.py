import re

regex1 = r'(@#+)(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)'
reg2 = r'(\d)'
num_lines = int(input())

while not num_lines == 0:

    line = input()
    barcodes = [item.group('barcode') for item in re.finditer(regex1, line)]

    if len(barcodes) == 0:
        print('Invalid barcode')

    for barcode in barcodes:
        group = [item.group() for item in re.finditer(reg2, barcode)]

        if len(group) == 0:
            print('Product group: 00')
        else:
            print(f'Product group: ', end="")
            print(*group, sep="")

    num_lines -= 1


