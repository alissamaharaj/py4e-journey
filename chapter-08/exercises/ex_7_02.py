fname = input("Enter file name: ")
fh = open(fname)

tot = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    conf = line.split()
    tot = tot + float(conf[1])

avg = tot/count
print('Average spam confidence:', avg)