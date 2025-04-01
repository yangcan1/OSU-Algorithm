import sys
import time

# Usage when run from the command line: python max_subarray_homework1.py <filename>.
# Example usage:                        python max_subarray_homework1.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()


def max_subarray_simplification_delegation(A):
    """
    Computes the value of a maximum subarray of the input array by "simplification and delegation."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    if len(A) == 1:
        return A[0]
    
    arr_left = A[: (len(A) - 1) // 2 + 1]
    arr_right = A[(len(A) - 1) // 2  + 1:]

    left_num = max_subarray_simplification_delegation(arr_left)
    right_num = max_subarray_simplification_delegation(arr_right)
    print(left_num, right_num)
    
    max_arr_left = -float('inf')
    max_arr_right = -float('inf')
    sum = 0
    for i in range((len(A) - 1) // 2, -1, -1):
        sum += A[i]
        if sum > max_arr_left:
            max_arr_left = sum

    sum = 0
    for i in range((len(A) - 1) // 2 + 1, len(A)):
        sum += A[i]
        if sum > max_arr_right:
            max_arr_right = sum

    return max([left_num, right_num, (max_arr_left + max_arr_right)])

    
def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in milliseconds.
    """

    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time
for alg in [max_subarray_simplification_delegation]:
    print(file_name, time_alg(alg, A))
    print(time_alg(alg, A))

