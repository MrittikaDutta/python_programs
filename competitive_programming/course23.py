def quicksort_median_of_three(arr):
    return _quicksort_median_of_three(arr, 0, len(arr) - 1)

def _quicksort_median_of_three(arr, low, high):
    comparisons = 0

    if low < high:
        # Choose the median of the first, middle, and final elements as the pivot
        pivot_index, comparisons_median_of_three = choose_median_of_three(arr, low, high)
        comparisons += comparisons_median_of_three

        # Move the pivot to the first position
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

        # Partition the array and get the index of the pivot element
        pivot_index_partition, comparisons_partition = partition_median_of_three(arr, low, high)
        comparisons += comparisons_partition

        # Recursively sort the subarrays
        comparisons += _quicksort_median_of_three(arr, low, pivot_index_partition - 1)
        comparisons += _quicksort_median_of_three(arr, pivot_index_partition + 1, high)

    return comparisons

def choose_median_of_three(arr, low, high):
    mid = (low + high) // 2

    # Compare the first, middle, and final elements
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid, 0
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low, 0
    else:
        return high, 0

def partition_median_of_three(arr, low, high):
    # Use the first element as the pivot
    pivot = arr[low]
    
    comparisons_partition = 0
    # Initialize pointers
    i = low + 1
    j = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Swap pivot with the rightmost element less than pivot
    arr[low], arr[i - 1] = arr[i - 1], arr[low]

    # Return the index of the pivot after partitioning and the number of comparisons made during partitioning
    return i - 1, high - low

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

# Example usage:
file_path = 'input.txt'  # Change this to the path of your input file
input_array = read_input_from_file(file_path)
comparisons = quicksort_median_of_three(input_array)
print(f"Sorted array: {input_array}")
print(f"Number of comparisons: {comparisons}")
