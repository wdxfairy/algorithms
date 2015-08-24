__author__ = 'wdxfairy'

def selection_sort(s):
    s_len = len(s)
    for i in range(s_len-1):
        min_num = s[i]
        min_index = i
        for j in range(i+1,s_len):
            if s[j] < min_num:
                min_num = s[j]
                min_index = j
        if min_num < s[i]:
            s[i], s[min_index] = s[min_index], s[i]

a = [1,2,3,4,3,2,1,4,5,6,6,7,8]

print(selection_sort(a))
print(a)

