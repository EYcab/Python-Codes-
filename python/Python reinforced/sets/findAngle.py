__author__ = 'Chenxi'
#!/usr/bin/python
#coding:utf-8
import sys,math
if sys.version_info[0]>=3: raw_input=input
d=int(raw_input())
b=int(raw_input())
a=math.hypot(d,b)/2
print(str(int(round(math.acos( b*b/(2*a*b) )*180/math.pi)))+'�')
#remember vector a*b*cos(theta)=b*b