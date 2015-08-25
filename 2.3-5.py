__author__ = 'wdxfairy'

__author__ = 'wdxfairy'

def findnum(v,s):
    L = len(s)
    start = 0
    end = L-1
    if L == 0:
        return None
    while 1:
        middle = (start + end)/2
        if s[middle] == v:
            return middle
        elif start == end:
            return None
        elif s[middle] < v:
            start = middle + 1
        elif s[middle] > v:
            end = middle


a = [5,1]
print(findnum(5,a))