def kadane( arr):
    m=arr[0]
    c=arr[0]
    for i in arr:
        c=max(i,c+1)
        m=max(m,c)
    return m
input_array = input("Enter the elements of the array separated by space: ")
nums = list(map(int, input_array.split()))
print(kadane(nums))