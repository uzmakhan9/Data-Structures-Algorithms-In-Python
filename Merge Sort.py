def merge_sort(arr1):
    if len(arr1)<=1:
        return
    mid=len(arr1)//2
    left=arr1[:mid]
    right=arr1[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_sorted_lists(left,right,arr1)

def merge_sorted_lists(a,b,arr2):
    i=j=k=0
    len_a=len(a)
    len_b=len(b)
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr2[k]=a[i]
            i+=1
        else:
            arr2[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr2[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr2[k]=b[j]
        j+=1
        k+=1

if __name__=="__main__":
    test_cases=[
        [45,7,86,5,34,21,13,18,9,3,100],
        [],
        [9],
        [9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9]
    ]
    for array in test_cases:
        merge_sort(array)
        print(array)
