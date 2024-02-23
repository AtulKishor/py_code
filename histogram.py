#import os
#print(os.path.join(os.path.abspath('.'),'bin','oo'))

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    print(count.setdefault(character, 0))
    count[character] += 1
pprint.pprint(count)

