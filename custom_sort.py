


def selection_sort(fruits): 
    for i in range(len(fruits)):
        min_strings=i
        for j in range(i+1,len(fruits)):
            if len(fruits[j])<len(fruits[min_strings]):
                min_strings=j
        fruits[i],fruits[min_strings]=fruits[min_strings],fruits[i]
    return fruits

fruits=["apple", "banana", "orange", "kiwi"]
get_min_strings_in_fruit=selection_sort(fruits)
print("Sorted fruits:",get_min_strings_in_fruit)

