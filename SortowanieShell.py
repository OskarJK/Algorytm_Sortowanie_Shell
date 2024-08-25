import time
import random
import math

def shell_sort(arr, gaps):
    n = len(arr)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

def generate_sequence(sequence_type, n):
    if sequence_type == "O(n^3/2)":
        return [n // int(k ** (3/2)) for k in range(1, int(n ** 0.5))]
    
    elif sequence_type == "O(n^4/3)":
        return [n // int(k ** (4/3)) for k in range(1, int(n ** (1/3)))]
    
    elif sequence_type == "O(n^2)":
        return [n // int(k ** 2) for k in range(1, n)]
    
    elif sequence_type == "O(log_n)":
        return [n // int(2 ** k) for k in range(1, int(math.log(n)))]
    
    elif sequence_type == "O(log2_n)":
        return [n // int(2 ** k) for k in range(1, int(math.log2(n)))]
    
    elif sequence_type == "O(n^13/3)":
        return [n // int(k ** (13/3)) for k in range(1, int(n ** (3 / 13)))]
    
    else:
        raise ValueError("Invalid sequence type")


def run_experiment(sequence_type, min_size, max_size, step):
    print(f"Running experiment for sequence type: {sequence_type}")
    for size in range(min_size, max_size + 1, step):
        arr = generate_random_array(size)
        gaps = generate_sequence(sequence_type, size)
        start_time = time.time()
        shell_sort(arr, gaps)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]



def main():
    min_size = 10000
    max_size = 500000
    step = 10000
    sequence_types = ["O(n^3/2)", "O(n^4/3)", "O(n^2)", "O(log_n)", "O(log2_n)", "O(n^13/3)"]
    
    for sequence_type in sequence_types:
        run_experiment(sequence_type, min_size, max_size, step)
        

if __name__ == "__main__":
    main()