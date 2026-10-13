import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
counts = info['comments']

nums = list()

for item in counts:
  nums.append(int(item['count']))

print('Count:', len(nums))
print('Sum:', sum(nums))
