# return all anagrams from text file
from collections import Counter
import collections

results = collections.defaultdict(str)
with open("anagram.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        results[str(sorted(Counter(line.rstrip()).items()))] += line.rstrip()+" "

for key, value in results.items():
    print(value[:-1])

"""
Uri's comments:
==============

* Very good! This code works.

"""
