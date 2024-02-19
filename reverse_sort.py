def reverse_sort(lst):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[j]>lst[min_index]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst
lst=[4,5,6,23,7,47]
reverse_sort_calculate=reverse_sort(lst)
print("Here is the reversed list:",reverse_sort_calculate)