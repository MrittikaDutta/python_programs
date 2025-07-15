def LCW(u,v):
    lcw=[]
    for r in range(len(u)+1):
        lcw[r][len(v)+1]=0
    for c in range(len(u)+1):
        lcw[len(u)+1][c]=0
    maxlcw=0
    for c in range(len(v)+1,-1,-1):
        for r in range(len(u)+1,-1,-1):
            if u[r]==v[c]:
                lcw[r][c]=1+lcw[r+1][c+1]
            else:
                lcw[r][c]=0
            if lcw[r][c]>maxlcw:
                maxlcw=lcw[r][c]
    return(maxlcw)
u="bisect"
v="insect"
print(LCW(u,v))