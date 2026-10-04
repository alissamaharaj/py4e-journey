name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

time = dict()

for line in handle:
    line = line.strip()
    words = line.split()
    if len(words) < 5 : continue
    if words[0] != "From": continue

    stamp = words[5]
    hour = stamp.split(":")
    if len(hour) != 3 : continue
    hour = hour[0]
    time[hour] = time.get(hour, 0) + 1

#print(time)
list = sorted(time.items())
#print(list)
for k,v in list:
    print(k,v)
    