fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w,0) + 1

# Find the word with the largest count

largest = None
bigword = None
for cle, valeur in many.items() :
    if largest is None or valeur > largest:
        largest = valeur
        bigword = cle

print(bigword, largest)
