
# def reve(a):
#     b=0
#     for i in range(len(a)):
#         # for j in range(i+1):
    
#         b = a[i]
#         a[i]=a[i+1]
#         a[i+1]=b
#     return(a)
# arr=[1,2,3,4,5,7,6,8,9]
# print(reve(arr))
def left_rotaion_by_n(a,n):
    b=a[n:] + a[:n]
    return(b)

ar=[23,34,56,8,90,5,3,54,22]
c=int(input())
# n=int(input())
# b=a[n:] + a[:n]
# return(b)
print(ar)
print(left_rotaion_by_n(ar,c))







