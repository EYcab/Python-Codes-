__author__ = 'Chenxi'
import sys,cmath
if sys.version_info[0]>=3: raw_input=input
c=eval(raw_input())
#print c
# get the complex form i+(num)*j

print(abs(c))
# the below Return phase of complex number z (also known as argument of z).
# i.e.
# >>> phase(complex(-1.0, 0.0))
# 3.1415926535897931
print(cmath.phase(c))