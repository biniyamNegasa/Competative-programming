n=int(input())
a=list(map(int,input().split()))
e=0
for num in a:
    if num%2==0:
        e+=1
if e!=0 and e!=n:
    print(*sorted(a))
else:
    print(*a)
