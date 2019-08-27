#!/bin/python3

def bin_search(a, e):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = int((hi+lo)/2)
        if e < a[mid]: hi = mid - 1
        elif e > a[mid]: lo = mid + 1
        else: return mid
    if e > a[mid]: mid += 1
    return mid

L = [1,2,3,4,5]
print(bin_search(L, 1))
print(bin_search(L, 2))
print(bin_search(L, 3))
print(bin_search(L, 4))
print(bin_search(L, 5))
