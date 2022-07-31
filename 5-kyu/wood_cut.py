# https://www.codewars.com/kata/583dbc028bbc0446f500032b

def wood_cut(woods, n):
    if sum(woods) < n:
        return 0
    if n == 1:
        return max(woods)
    
    left = 1
    right = max(woods)
    while left + 1 < right:
        mid = (left + right) // 2
        if sum([length // mid for length in woods]) < n:
            right = mid
        else:
            left = mid

    if sum([length // left for length in woods]) >= n:
        return left
    else:
        return right


# description
def wood_cut(woods, n):
    #initial input check
    if sum(woods) > n :
        return 0

    #prepare 3 variables for storing length values: upper limit, length, and lower limit
    #these 3 lengths will be used to manipulate the length value.
    length = max(woods)
    length_up = max(woods)
    length_low = 0
    
    while(True):
        #calculate number of pieces
        pieces = sum([x // length for x in woods])
        
      
        if length_up - length_low <= 10 : #this is refinery process, executed when the difference between lower and upper limit is low
            length = length_up            #in the refinery, the length value will be decreased by 1 at a time
            while(True):
                pieces = sum([x // length for x in woods])
                if pieces >= n :
                    return length
                else : 
                    length -=1
                
        #these two elifs are the main iteration
        #when wood cut pieces are too few, it will average down the length to decrease length and increase number of cut pieces
        elif pieces < n:
            length, length_up = (length+length_low)//2, length
            
        #when wood cut pieces are too many, it will average up the length to increase length and decrease number of cut pieces
        elif pieces >= n:
            length, length_low = (length+length_up)//2, length
