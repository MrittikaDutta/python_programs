y=int(input("enter year"))
flag=False
if y%400==0:
    flag=True
elif y%4==0 and y%100!=0:
    flag=True
if flag:
    print("leap year")
else:
    print("not leap year")