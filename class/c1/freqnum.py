def freq():
    lst = []
    frequency = 0
    n = int(input("Enter the number of elements : "))
    print("Enter the elements : ")
    for i in range(0,n):
        elem = int(input())
        lst.append(elem)
    num = int(input("Enter the value : "))
    for i in range(0,len(lst)):
        if(num == lst[i]):
            frequency += 1
    print(f"{num} is repeated {frequency} times")

freq()