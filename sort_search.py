#goal
#selection_sort
#binary_search

def selection_sort(lst):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if(lst[j]<lst[min_index]):
                min_index=j
        #swap the old list and new lsit
        #using a tuple
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst
 #Test case
lst=[123,78,23,99,101]
check_sorted_list=selection_sort(lst)
print("The sorted list is:",check_sorted_list)