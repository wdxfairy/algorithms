__author__ = 'wdxfairy'

def merge(a,b):
    c = []
    while a and b:
        if a[0]>b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    if a:
        c += a
    if b:
        c += b
    return c

a = [1, 2, 3, 4, 5, 7]
b = [1, 3, 4, 6]

print(merge(a,b))