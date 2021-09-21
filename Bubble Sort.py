# you can use this code to sort strings too

def bubble_sort(arr):
    size=len(arr)
    
    for i in range(size-1):
        swapped=False
        
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
                swapped=True
        
        if not swapped:
            break

if __name__=="__main__":
    elements=[
        [5,9,2,1,67,34,88,34],
        [1,2,3,4,2],
        ["mona","dhaval","aamir","Aamir","tina","chang"]
    ]
    for array in elements:
        bubble_sort(array)
        print(array)