__author__ = 'Chenxi'
import re
lst = list()
for i in range(int(raw_input())):
    lst.append(raw_input())
print sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst)))

#
# Attention here:
# lst = list()
# so we could have a list

#Notes:
# lst = []--------------is a arr not a list
