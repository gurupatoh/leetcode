def sort_tuples(lst,index):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if(lst[j][index]<lst[min_index][index]):
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst
# Test case
tuples_list = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_tuples = sort_tuples(tuples_list, 0)  # Sort based on the first element of each tuple
print("Sorted tuples:", sorted_tuples)
