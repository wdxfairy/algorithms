__author__ = 'wdx'


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def max_heapify(a, i):
    largest = i+1
    nummax = len(a)
    num = i
    while largest != num:
        largest = num
        if left(num) > nummax - 1:
            pass
        elif a[left(num)] > a[num]:
            largest = left(num)           
        
        if right(num)> nummax - 1:
            pass
        elif a[right(num)] > a[num] and a[right(num)] > a[left(num)]:
            largest = right(num)

        if largest != num:
            a[num], a[largest] = a[largest], a[num]
            num = largest
            largest += 1

A = [1,5,3,2,4]
max_heapify(A, 0)
print(A)



        
        
