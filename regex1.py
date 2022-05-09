import re
name  = input("Enter  file: ")
if len(name) <1: 
    name = "regex_sum_42.txt"
handle = open(name)
numlist = list()

for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    num = int(num)
    numlist.append(num)
print(numlist)
