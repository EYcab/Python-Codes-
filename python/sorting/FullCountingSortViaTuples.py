#!/usr/bin/python2.7


def mySort(tupledArray):
    '''
    Sort the given array according to the first element (an integer) of each tuple.  Do this stably.
    tupledArray[x][0] = original integer -- sort using this
    tupledArray[x][0] = original string
    tupledArray[x][0] = original position -- maintain stability using this
    '''

    #take advantage of python's built-in sorting functions
    return sorted(tupledArray, key=lambda element: element[0])

if __name__ == '__main__':

    #number of elements
    totalElements = int(raw_input())

    rawArray = [raw_input() for x in range(totalElements)]

    '''
    tupledArray[x][0] = original integer
    tupledArray[x][0] = original string
    tupledArray[x][0] = original position
    '''
    tupledArray = []
    
    #read each line of input and create a tuple of one integer + one string
    for position in range(totalElements):
        theInt, theString = rawArray[position].split(' ')
        #append a tuple
        tupledArray.append( (int(theInt), theString, position,) )

    sortedArray = mySort(tupledArray)

    #print elements that occur in second half of array
    for element in sortedArray:
        if element[2] >= totalElements/2:
            print element[1],
        else:
            print '-',