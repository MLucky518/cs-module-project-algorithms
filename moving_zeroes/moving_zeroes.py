'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # For every array element in the length of given array iterate and check if value is equal to 0
    # If equal, we remove the element and append a 0 to the end of our array essentially moving non zero ints left

    for i in range(0,len(arr)):
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")