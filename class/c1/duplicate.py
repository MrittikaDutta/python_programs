def duplicate(l):
    le=len(l)
    for i in range(le):
        for j in range(i+1,le):
            if l[i]==l[j]:
                return True
    return False


n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    a=int(input("enter an element :"))
    l.append(a)
if duplicate(l):
    print("Duplicate elements present")
else:
    print("Duplicate elements absent")
