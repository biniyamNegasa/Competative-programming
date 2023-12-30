class RandomizedSet:

    def __init__(self):
        self.s={}
        self.l=[]
        self.c=0

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val]=self.c
        self.l.append(val)
        self.c+=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        c=self.s[val]
        self.s[self.l[-1]]=c
        self.l[self.s[val]],self.l[-1]=self.l[-1],self.l[self.s[val]]
        
        self.l.pop()
        self.s.pop(val)
        self.c-=1
        return True

    def getRandom(self) -> int:
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()