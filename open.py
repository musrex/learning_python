# fhand = open('ilovecordelia.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('I'):
#         continue
#     print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(fname, 'r')
except: 
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    
    print(line)