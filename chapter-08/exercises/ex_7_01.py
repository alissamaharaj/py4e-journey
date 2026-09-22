
fh = open('mbox.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())