name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
address=list()

emails = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        address.append(line[1])

for contact in address:
    emails[contact] =  emails.get(contact, 0) + 1

most = None
count = None
for contact in emails:
    if count == None or count < emails[contact]:
        most = contact
        count = emails[contact]
print(most, count)

