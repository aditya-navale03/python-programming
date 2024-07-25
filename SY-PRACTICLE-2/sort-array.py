#Q.sort tuple in acending and decending order 5,-3,0,1,6,-6
def tuple_sort(tup):
    n = len(tup)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tup[j] > tup[j + 1]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]

ot = (5, -3, 0, 1, 6, -6)
st = list(ot) 
tuple_sort(st)
sorted_tuple_asc = tuple(st)  
print("Ascending order (manual):", sorted_tuple_asc)
