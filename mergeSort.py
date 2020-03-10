def merge(a,b):
    c=[]
    (i,j)=(0,0)
    while (i+j)<(len(a)+len(b)):
        if i==len(a):
            c.append(b[j])
            j = j +1
        elif j==len(b):
            c.append(a[i])
            i = i+1
        elif a[i]<b[j]:
            c.append(a[i])
            i=i+1

        elif(b[j]<a[i]):
            c.append(b[j])
            j=j+1
    return c


def mergeSort(c,left,right):
    if right-left <= 1:
        return (c[left:right])
    if right-left>1:
        mid=(right+left)//2
        L=mergeSort(c,left,mid)
        R=mergeSort(c,mid,right)
        return merge(L,R)
a=[1,2,4,3]
b=[343,53,11,10]
h=merge(a,b)
print(h)
c=mergeSort(h,0,len(h))
print(c)






