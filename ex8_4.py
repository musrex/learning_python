fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = []
for line in fh:
    lst.append(line.split())

for word in lst:
    if word not in lst2:
        lst2.append(word)

lst2 = lst[0] + lst[1] + lst[2] + lst[3]

words = []
for word in lst2:
    if word not in words:
         words.append(word)

words.sort()
print(words)    
