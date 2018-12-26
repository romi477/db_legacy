import time
import os
import datetime
import json
import collections
from pprint import pprint

f = r'..\scc2_legacy\cinemas\fixtures\cinemas7.json'

with open(f, 'r') as file:
    j = json.load(file)


lst = [i['fields']['slug'] for i in j]

c = collections.Counter()

for value in lst:
    c[value] += 1

pprint(c)
