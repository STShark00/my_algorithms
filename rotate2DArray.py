''' Rotate n x n 2D Matrix by 90 degrees (clockwise) '''
def rotateImage(a):
    n = len(a)
    
    result = [[] for _ in range(n)]
    while len(a) > 0:
        lst = a.pop()
        i = 0
        for elem in lst:
            result[i].append(elem)
            i += 1
    return result