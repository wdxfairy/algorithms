__author__ = 'wdxfairy'

def insertion_sort(s):
    L = len(s)
    for i in range(1, L):
        key = s[i]
        for j in range(i):
            if s[i-j-1] < key:
                s[i-j] = s[i-j-1]
            else:
                s[i-j] = key
                break
        else:
            s[0] = key

a = [2,3,4,5,6,3,4,5,7]
insertion_sort(a)
print a


