#!/bin/python3

# def bsearch(a, e):
#     lo, hi = 0, len(a)-1
#     while lo <= hi:
#         mid = (hi+lo)//2
#         if e < a[mid]: hi = mid - 1
#         elif e > a[mid]: lo = mid + 1
#         else: return mid
#     return -1

def bsearch(a, e): # return index to insert
    if e < a[0]: return 0
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (hi+lo)//2
        if e < a[mid]: hi = mid - 1
        elif e > a[mid]: lo = mid + 1
        else: return mid + 1
    return lo

def bisect(a, e):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (hi+lo)//2
        if e < a[mid]: hi = mid
        else: lo = mid + 1
    return lo

# L = [1,3,5,7,9,10]
L = [2,4,6,8]
print(bsearch(L, 1), bisect(L, 1))
print(bsearch(L, 3), bisect(L, 3))
print(bsearch(L, 5), bisect(L, 5))
print(bsearch(L, 7), bisect(L, 7))
print(bsearch(L, 9), bisect(L, 9))
