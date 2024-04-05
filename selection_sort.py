grades=[56,76,88,90,34,45]
for i in range(len(grades)):
    #initialize minium index
    min_index=i
    for j in range(i+1,len(grades)):
        if(grades[j]<grades[min_index]):
            min_index=j
    grades[i],grades[min_index]=grades[min_index],grades[i]
print("Sorted list of grades is :",grades)

