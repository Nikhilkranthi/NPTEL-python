def selection_sort(l):
    for i in range(0, len(l)):
        min_element = i
        for j in range(i, len(l)):
            if l[j] < l[min_element]:
                min_element = j
        (l[i], l[min_element]) = (l[min_element], l[i])
    return l


test = list(range(1000, -1, -1))
print(selection_sort(test))


# complexity= O(n^2)
# For a python code to complete in 1 sec = 10^7 steps (Maximum)
