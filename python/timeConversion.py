#!/usr/bin/py
from datetime import datetime
 
def convertToEuTime(us_time):
    return datetime.strptime(us_time, '%I:%M:%S%p').strftime('%H:%M:%S')
 
 
if __name__ == '__main__':
    us_time = raw_input()
    print convertToEuTime(us_time)