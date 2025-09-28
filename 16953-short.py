def s(i,c):
    if i>B:return -1
    elif i<B:return max(s(i*2,c+1),s(i*10+1,c+1))
    return c
A,B=map(int,input().split())
print(s(A,1))