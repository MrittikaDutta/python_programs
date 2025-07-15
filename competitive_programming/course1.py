def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, split_inv = merge_and_count(left, right)

    return merged, inv_left + inv_right + split_inv

def merge_and_count(left, right):
    result = []
    i = j = split_inv = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            split_inv += len(left) - i
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, split_inv

with open('your_file.txt', 'r') as file:
    array = [int(line.strip()) for line in file]

sorted_array, inversions = count_inversions(array)
print(inversions)
