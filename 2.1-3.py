__author__ = 'wdxfairy'

def findnum(v,s):
    L = len(s)
    for i in range(L):
        if s[i] == v:
            return i
    return None

a = [1,3,54,7,3,2,5,2]
print(findnum(54,a))