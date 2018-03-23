import re
name = input("please input you flie name ")
text = open(name)
total = 0
for line in text:
    str_number = re.findall("[0-9]+", line)
    if len(str_number) == 0:
        continue
    for number in str_number:
        total += int(number)
print(total)
