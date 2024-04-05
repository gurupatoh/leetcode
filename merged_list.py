list1 = [1, 3, 5,7]
list2 = [2, 4, 6,10]

lst=list1+list2
print("The merged list is:",lst)
def selection_sort(lst):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_index]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst

test_selection_sort=selection_sort(lst)
print("The sorted list is:",test_selection_sort)

def binary_search(lst):
    low=0
    high=len(lst)-1
    while(low<=high):
        mid=(low+high)//2
        
        if (len(lst)%2==0):
            return (lst[mid]+lst[mid+1])/2
        elif (len(lst)%2==1):
            return lst[mid]
        
test_binary_search=binary_search(lst)
print("The median is:",test_binary_search)
        