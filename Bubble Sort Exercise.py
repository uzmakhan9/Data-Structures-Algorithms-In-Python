# you can use this code to sort strings too

def bubble_sort(arr,key):
    size=len(arr)
    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if arr[j][key]>arr[j+1][key]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
                swapped=True
        if not swapped:
            break
    return arr

if __name__=="__main__":
    elements=[
        {'name':'mona','transaction_amount':1000,'device':'iphone-10'},
        {'name':'dhaval','transaction_amount':400,'device':'google-pixel'},
        {'name':'kathy','transaction_amount':200,'device':'vivo'},
        {'name':'aamir','transaction_amount':800,'device':'iphone-10'}
    ]
    print(bubble_sort(elements,key='transaction_amount'))
