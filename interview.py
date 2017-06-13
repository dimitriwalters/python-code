def isPalindrome(s):
    return s == s[::-1]

print isPalindrome('hai')
print isPalindrome('racecar')

def isDuplicates(arr):
    h = {}
    for a in arr:
        if a in h: return True
        h[a] = 1
    return False

print isDuplicates([1,2,3])
print isDuplicates([1,2,3,1])

def isBalanced(s):
    arr = []
    for c in s:
        if c == '(':
            arr.append(c)
        else:
            if not arr: return False
            arr.pop()
    return not arr

print isBalanced('()()(')
print isBalanced(')()()')
print isBalanced('()()()')
