def find_kth_smallest(grades,k):
    for i in range(k):
        min_index=i
        for j in range(i+1,len(grades)):
           if (grades[j]<grades[min_index]):
               min_index=j
        grades[i],grades[min_index]=grades[min_index],grades[i]
    return grades[k-1]
# Define the test case
grades = [18, 29, 35, 33, 21, 19, 12, 15]
k=1
print("snallest  element:", find_kth_smallest(grades,k))

