fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])