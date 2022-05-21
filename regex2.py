import re
handle = open('regex_sum_1483550.txt')
val=0

for line in handle:
    num = re.findall('[0-9]+', line)
    for x in num:
        x = int(x)
        val = x + val

print(val)
