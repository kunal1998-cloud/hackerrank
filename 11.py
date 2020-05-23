def findword(s,w):
    needle = w
    idx_in_needle = 0
    for c in s:
        if c == needle[idx_in_needle]:
            idx_in_needle += 1
        if idx_in_needle == len(needle):
            break
             
    if idx_in_needle == len(needle):
        return "YES"
    else: 
        return "NO"
w=input("Enter word w/c u want to search")
s=input("enter word in w/c u want to search")
print(findword(s,w))