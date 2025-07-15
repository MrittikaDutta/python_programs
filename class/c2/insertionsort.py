n = int(input("Enter the number of elements in a list: "))
l = []

for i in range(n):
    g = int(input("Enter element: "))
    l.append(g)

for i in range(1, n):
    key = l[i]
    j = i - 1

    while j >= 0 and key < l[j]:
        l[j + 1] = l[j]
        j -= 1

    l[j + 1] = key

print("Sorted list:")
for i in range(n):
    print(l[i], end=" ")
