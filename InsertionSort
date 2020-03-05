def insertion_sort(l):
    for i in range(0,len(l)):
        pos=i;
        while((pos>0) and (l[pos]<l[pos-1])):
            (l[pos], l[pos-1]) = (l[pos-1], l[pos])
            pos=pos-1;

    return l
l=list(range(500,1,-1))
print(insertion_sort(l))

# Complexity same as Selection SOrt
