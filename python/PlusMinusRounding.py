#!/usr/bin/py
 
def getPartitionPythonesque(values):
    c1 = len(filter(lambda x:x>0,values))
    c2 = len(filter(lambda x:x<0,values))
    c3 = len(filter(lambda x:x==0,values))
    v_len = float(len(values))
     
    return (c1/v_len, c2/v_len, c3/v_len)
----------------------------------------------------------    
 
def getPartition(values):
    pos, neg, zero = [0.0,0.0,0.0]
    v_len = len(values)
     
    for value in values:
        if value == 0:  zero += 1
        elif value > 0: pos += 1
        else:           neg += 1
             
    return (pos/v_len, neg/v_len, zero/v_len)    
     
 
if __name__ == '__main__':
    t = input()
    values = map(int, raw_input().split())
    partition = getPartition(values)
    #or partition = getPartitionPythonesque(values)
    for percentage in partition:
        print round(percentage,4)