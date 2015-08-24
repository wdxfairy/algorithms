__author__ = 'wdxfairy'

def binadd(a,b):
    L =len(a)
    c = [0] * (L+1)
    key = 0
    for i in range(L):
        x = L-i-1
        c[x+1] = (a[x] +b[x] +key)%2
        key = (a[x] +b[x] +key)//2
    c[0] = key
    return c

a = [0,1,1,0,1,0,1]
b = [1,0,1,1,0,1,0]

print (binadd(a,b))
