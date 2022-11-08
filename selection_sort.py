def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[min_index]>my_list[j]:
                min_index=j
        if i!=min_index:
            my_list[i],my_list[min_index]=my_list[min_index],my_list[i]
    return my_list

print(selection_sort([10, 2, 31, 4, 5, 6]))