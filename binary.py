def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

sorted_array = [1, 13, 56, 101, 155, 189]  # Sorted array
item_to_find = 101

index = binary_search(sorted_array, item_to_find)
if index is not None:
    print("The item", item_to_find, "is at index:", index)
else:
    print("The item", item_to_find, "is not found in the array.")
