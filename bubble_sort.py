def bubble_sort(my_list):
    for j in range(len(my_list)-1,0,-1):
        for i in range(j):
            if my_list[i]>my_list[i+1]:
                my_list[i+1],my_list[i] = my_list[i],my_list[i + 1]
    return my_list

print(bubble_sort([8,9,7,4,2,6,5,1,3]))