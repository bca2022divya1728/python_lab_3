def sequential_search(arr,target):
    
    for index in range(len(arr)):
       
        if arr[index]==target:
            return index
    return -1
    
elements=[1, 3, 5, 8, 10, 23, 35]
search_target= 10

result=sequential_search(elements,search_target)

if result != -1:
    print(f"Element {search_target} found at index {result}.")
else:
    print(f"Element {search_target} not found in the list.")
