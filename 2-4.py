__author__ = 'wdxfairy'


def inversion(s):
    L = len(s)
    num = 0
    if L <= 1:
        return 0
    else:
        mid = L/2
        num += inversion(s[:mid])
        num += inversion(s[mid:L])
        num += merge(s,mid,L)
    return num


def merge(s, p, Length):
    left = s[:p]
    right= s[p:Length]
    c = []
    numleft = p
    num = 0
    while left and right:
        if left[0] < right[0]:
            numleft -= 1
            c.append(left[0])
            left.pop(0)
        else:
            c.append(right[0])
            num += numleft
            right.pop(0)
    if left:
        c += left
    if right:
        c += right
    s[:] = c[:]
    return num

a = [ 3, 2, 4]
print(inversion(a))




