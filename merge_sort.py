def merge(l1,l2):
    result=[]
    i=j=0
    while i< len(l1) and j < len(l2):
        if l1[i]<l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    while i < len(l1):
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1
    return result

def merge_sort(my_list):
    if len(my_list) == 1:return my_list
    m = len(my_list) // 2
    return merge(merge_sort(my_list[:m]),merge_sort(my_list[m:]))

print(merge_sort([3,6,1,2,5,4,8,7]))
#print(merge([1,2,7,8],[3,4,5,6]))
