import re

file = open('regex_sum_2469137.txt')

tot = None

for line in file:
    line = line.strip()
    nums = re.findall('[0-9]+', line)
    
    for num in nums:
        num = int(num)
        if tot is None: tot = num
        else: tot = tot + num
print(tot)

# Now for the fun practice part, trying to condense into one line of code.

#print(sum((int(num) for line in file for num in re.findall('[0-9]+', line))))

print(sum(int(num) for num in re.findall('[0-9]+',open('regex_sum_2469137.txt').read() )))
