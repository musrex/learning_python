name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
address = list()
emails = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        address = line[1]

for addess in line:
    if address not in emails:
                emails[address] = emails.get(address, 0) + 1

maxe = 0
for key in emails:
    if emails[key] > maxe:
        maxe = key

print(emails, emails[maxe])

        
        #emails[address] = emails.get(address, 0) + 1
        
#print(emails)

