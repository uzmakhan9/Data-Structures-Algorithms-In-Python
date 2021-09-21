def merge_sort(elements,key,descending):
    size=len(elements)
    if size<=1:
        return elements
    mid=size//2
    left=elements[:mid]
    right=elements[mid:]
    left_list=merge_sort(left,key,descending)
    right_list=merge_sort(right,key,descending)
    sorted_list=merge_sorted_lists(left_list,right_list,key,descending)
    return sorted_list

def merge_sorted_lists(left_list,right_list,key,descending):
    i=j=0
    merged=[]
    if descending:
        while len(left_list)>i and len(right_list)>j:
            if left_list[i][key]>=right_list[j][key]:
                merged.append(left_list.pop(i))
            else:
                merged.append(right_list.pop(j))
    else:
        while len(left_list)>i and len(right_list)>j:
            if left_list[i][key]<=right_list[j][key]:
                merged.append(left_list.pop(i))
            else:
                merged.append(right_list.pop(j))
    
    merged.extend(left_list)
    merged.extend(right_list)
    return merged

if __name__=="__main__":
    elements=[
        {'name':'vedanth','age':17,'time_hours':1},
        {'name':'rajab','age':12,'time_hours':3},
        {'name':'vignesh','age':21,'time_hours':2.5},
        {'name':'chinmay','age':24,'time_hours':1.5},
    ]
    print(merge_sort(elements,key='time_hours',descending=True))
    # print(sorted_list)
