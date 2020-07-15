'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
#O(1)space

# get length of given array
    length = len(arr)

# initialize array with amount of elements equal to length of input array

    product = [0] * length

# there are no elements to the left of the first element so set product[0] to one
    product[0] = 1

# finding product of elements to the left of current index 
    for i in range(1,length-1):
        product[i] = arr[i-1] * product[i-1]


    right = 1

    for i in reversed(range(length)):
        product[i] = product[i] * right
        right *= arr[i]
    return product





#O(n)


# # The length of the input array 
#     length = len(arr)
# # arrays to seperate values to the left and right of the current array index to be left out
#     left,right,product = [0] * length,[0] * length,[0] * length

#     left[0] = 1

#     for i in range(1,length):
#         left[i] = arr[i-1] * left[i-1]
    
#     right[length-1] = 1

#     for i in reversed(range(length-1)):
#         right[i] = arr[i+1] * right[i+1]

#     for i in range(length):
#         product[i] = left[i] * right[i]

#     return product




                

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
