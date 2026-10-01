name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

mail = dict()

for line in handle:
    line = line.strip()
    words = line.split()
    if len(words) < 2 :
        continue
    if words[0] != "From":
        continue

    word = words[1]
    mail[word] = mail.get(word,0) + 1
        
bigname = None
bigcount = None
for most,value in mail.items():
    if bigname is None or value > bigcount:
        bigname = most
        bigcount = value
        
print(bigname, bigcount)
