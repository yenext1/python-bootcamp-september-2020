x = [10 ,999,20,30]

dir(x) #will shoe all methods for list

x.append(50)

x.pop()

x.insert(1,999)
x.remove(999)

help(x.remove)

for i , digit in enumerate(x):
    print (f"{index}) {digit}")


10 in x # true / false

high_grades_only = [g for g in grades if g > 80]

tuples
p1 = (20,20)


shapes = {
    'triangle': 3,
    "rectangle":4

}


for key, val in shapes.items():
    print(f"{key} => {val}")


for val in shapes.values():
    print(val);


words = {
    'a': ['airplace', 'age'],
    'b': ["banana"]
}

word_count_by_letter = {
    key = len(val)
    for key, val in words.items()
}

import glob
import os.path
import collections

all_filles_with_extensions = glob.glob('*.*')
print(all_filles_with_extensions)

#base, ext = os.path.splitext("demo1.py")

#counter = {}
counter = collections.defaultdict(int)
for filename in all_filles_with_extensions:
     , ext = os.path.splitext(filename)
     counter[ext] += 1
     '''
     try:
        counter[ext] += 1
     except KeyError:
        counter[ext] = 1
        '''


s = set([10 ,20])

import fileinput

for line in fileinput('story.txt'):
    print(f" {line}", end="" )


import collections

Point = collections.namedtuple('Point', ['x','y'])


c = collections.Counter()
c.update([10,20,30,20,20,10]) # Counter({20: 3, 10: 2, 30:1})


extensions = [
    os.path.splitext(fname)[1]
    for fname in all_filles_with_extensions
]