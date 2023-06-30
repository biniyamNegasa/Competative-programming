n,k=map(int,input().split())
m=list(map(int,input().split()))
m.sort()
x=m[k-1]
def o(m,k,x):
	if k==0:
		return m[k]-1 if m[k]>1 else -1
	for i in m[k:]:
		if i<=x:
			return -1
	return x
print(o(m,k,x))
