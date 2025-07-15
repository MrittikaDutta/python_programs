def leap(y):
    flag=False
    if y%400==0:
        flag=True
    elif y%4==0 and y%100!=0:
        flag=True
    if flag:
        return(29)
    else:
        return 28
a=int(input("enter month number: "))
yr=int(input("enter year :"))
m=["INVALID",31,leap(yr),31,30,31,30,31,31,30,31,30,31]
if a>12:
    print("INVALID")
else:
    for i in range(len(m)):
        if a==i:
            print(m[i])