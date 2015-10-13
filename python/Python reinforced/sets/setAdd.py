__author__ = 'Chenxi'
import sys
if sys.version_info[0]>=3: raw_input=input
a=set.add(raw_input() for _ in range(int(raw_input())))
print(len(a))

# for the below input:
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
