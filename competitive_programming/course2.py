def quicksort(arr):
    return _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
    comparisons = 0

    if low < high:
        # Partition the array and get the index of the pivot element
        pivot_index, comparisons_partition = partition(arr, low, high)
        comparisons += comparisons_partition

        # Recursively sort the subarrays
        comparisons += _quicksort(arr, low, pivot_index - 1)
        comparisons += _quicksort(arr, pivot_index + 1, high)

    return comparisons

def partition(arr, low, high):
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
comparisons = quicksort(input_array)
print(f"Sorted array: {input_array}")
print(f"Number of comparisons: {comparisons}")

