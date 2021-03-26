#https://www.hackerrank.com/challenges/list-comprehensions/problem

res=[]
x=int(input())
y=int(input())
z=int(input())
n=int(input())
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if((i+j+k)!=n):
                x=[i,j,k]
                res.append(x)
print(res)
