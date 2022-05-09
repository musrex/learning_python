name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hour = list()
count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        line2 = line[5]
        hour.append(line2[0:2])

for time in hour:
    count[time] = count.get(time, 0) +1

for k, v in sorted(count.items()):
    print(k,v)
