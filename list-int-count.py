# Script to count integers in a list.

#!/usr/bin/env python3

from fibonacci2 import fibseq  # type: ignore
import operator

#list1 = [1234, 5678, 9012, 3456, 7890, 1234]

list1 = [fibseq(5)]

int_count = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for x in list1:
    for y in str(x):
        if y not in int_count:
            continue
        else:
            int_count[y] += 1
#print(int_count)

sorted_d = sorted(int_count.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)

'''
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
'''