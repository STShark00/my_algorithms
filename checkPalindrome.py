def checkPalindrome(inputString):
    
    return inputString == inputString[::-1]

    ''' Alternative Solution'''
    '''
    length = len(inputString)
    
    for i in range((length+1) // 2):
        if inputString[i] != inputString[length-1-i]:
            return False
    return True
    '''
