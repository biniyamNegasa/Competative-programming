class OrderedStream:

    def __init__(self, n: int):
        self.dic={i+1:'' for i in range(1000)}
        self.ptr=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey]=value
        if self.dic[self.ptr]:
            arr=[]
            temp=self.ptr
            while self.dic[temp] and temp<1001:
                arr.append(self.dic[temp])
                temp+=1
            self.ptr=temp
            return arr



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)