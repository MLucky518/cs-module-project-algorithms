'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Sort the given array for easier traversal and comparing
    # loop through array elements by two each iteration comparing if the elments are equal
    # If eual the loop continues to end, if not equal we return the value that is different 
    # Naive approach 
    arr.sort()
    for i in range(0,len(arr)-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]
       
        



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")