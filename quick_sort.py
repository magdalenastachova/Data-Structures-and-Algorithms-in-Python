def pivot(my_list,pivot_index,end_index):
    grey=pivot_index
    for i in range(pivot_index+1,end_index+1):
        if my_list[pivot_index]>my_list[i]:
            grey += 1
            if i != grey: my_list[i],my_list[grey]=my_list[grey],my_list[i]
    my_list[pivot_index],my_list[grey]=my_list[grey],my_list[pivot_index]
    return grey

def quick_sort_helper(inp,left,right):
    if left < right:
        pivot_index=pivot(inp,left,right)
        quick_sort_helper(inp,left,pivot_index-1)
        quick_sort_helper(inp, pivot_index +1, right)
    return inp

def quick_sort(input_list):
    return quick_sort_helper(input_list,0,len(input_list)-1)

print(quick_sort([4,6,1,7,3,2,5]))