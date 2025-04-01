import sys
import time

A = 1234435435
B = 567867787889998978989

def multipli(num1, num2):
    return num1 * num2

def time_alg(A, B):
    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = A * B
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time

print(time_alg(A, B))