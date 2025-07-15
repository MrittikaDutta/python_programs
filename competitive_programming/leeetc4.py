
s="abc"
def ispal(st):
    return st==st[::-1]
n=len(s)
for i in range(n):
    s1=s[:i]+s[i+1:]
    if ispal(s1):
        print(s1)
#         return True
# return False