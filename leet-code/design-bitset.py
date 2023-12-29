class Bitset:

    def __init__(self, size: int):
        self.arr=[0]*size
        self.fl=0
        self.c=0
        self.l=defaultdict(int)
        self.l[0]=size

    def fix(self, idx: int) -> None:
        if self.fl%2:
            if self.arr[idx]:
                self.arr[idx]=0
                self.c+=1
                self.l[1]+=1
                if self.l[0]==1:
                    del self.l[0]
                else:
                    self.l[0]-=1
        else:
            if not self.arr[idx]:
                self.arr[idx]=1
                self.c+=1
                self.l[1]+=1
                if self.l[0]==1:
                    del self.l[0]
                else:
                    self.l[0]-=1
            

    def unfix(self, idx: int) -> None:
        if self.fl%2:
            if not self.arr[idx]:
                self.arr[idx]=1
                self.c-=1
                self.l[0]+=1
                if self.l[1]==1:
                    del self.l[1]
                else:
                    self.l[1]-=1
                    
        else:
            if self.arr[idx]:
                self.arr[idx]=0
                self.c-=1
                self.l[0]+=1
                if self.l[1]==1:
                    del self.l[1]
                else:
                    self.l[1]-=1

    def flip(self) -> None:
        self.fl+=1
        self.c=len(self.arr)-self.c
        self.l[0]=len(self.arr)-self.c
        self.l[1]=self.c

    def all(self) -> bool:
        return not self.l[0] and self.l[1]

    def one(self) -> bool:
        return self.l[1]

    def count(self) -> int:
        return self.c

    def toString(self) -> str:
        if self.fl%2:
            return ''.join([str(1-n) for n in self.arr])
        return ''.join([str(n) for n in self.arr])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()