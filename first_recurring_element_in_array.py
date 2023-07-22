
# First Recurring Element in Array

arr = [1, 4, 5, 4, 3, 2, 0]

def get_first_recurring_in_array(arr):
    arr_count = len(arr)
    
    for i, item in enumerate(arr):
        orig_item = item % arr_count

        if item >= (arr_count * 2):
            print('Item found...', i)
            break
        else:
            arr[orig_item] += arr_count
    
get_first_recurring_in_array(arr)
