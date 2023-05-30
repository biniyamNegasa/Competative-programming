if __name__ == '__main__':
    N = int(input())
    b=[]
    for i in range(N):
        c=input().split()
        if c[0]=="insert":
            b.insert(int(c[1]),int(c[2]))
        elif c[0]=="print":
            print(b)
        elif c[0]=="remove":
            b.remove(int(c[1]))
        elif c[0]=="sort":
            b.sort()
        elif c[0]=="append":
            b.append(int(c[1]))
        elif c[0]=="pop":
            b.pop()
        else:
            b.reverse()
