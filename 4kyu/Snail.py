# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(array):
    snail_result = []
    while array:
        # append the first row from left to right
        snail_result.extend(array.pop(0))
        
        # append the last element from each remaining row
        if array and array[0]:
            for row in array:
                snail_result.append(row.pop(-1))
        
        # append the last row from right to left
        if array:
            snail_result.extend(array.pop(-1)[::-1])
        
        # append the first element from each remaining row
        if array and array[0]:
            for row in array[::-1]:
                snail_result.append(row.pop(0))
    
    # Check if the middle row exists
    if array and array[0]:
        middle_row = array[len(array) // 2]
        # Add the middle row in reverse order if it has an odd number of elements
        if len(middle_row) % 2 != 0:
            snail_result.extend(middle_row[::-1])
        # Add the middle row as is if it has an even number of elements
        else:
            snail_result.extend(middle_row)
    
    return snail_result

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array) == expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array) == expected)