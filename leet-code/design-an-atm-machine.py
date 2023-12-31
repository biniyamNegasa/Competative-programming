class ATM:

    def __init__(self):
        self.notes=[0 for i in range(5)] 
        self.birr=[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,n in enumerate(banknotesCount):
            self.notes[i]+=n

    def withdraw(self, amount: int) -> List[int]:
        temp=[0 for i in range(5)]
        r=-1
        x=amount
        for i in range(4,-1,-1):
            if self.notes[i]>0 and amount>=self.birr[i]:
                val=amount//self.birr[i]
                r=amount%self.birr[i]
                if val>self.notes[i]:
                    temp[i]=self.notes[i]
                    amount=(val-temp[i])*self.birr[i]+r
                else:
                    temp[i]=val
                    amount=r
        pr=0
        for i in range(5):
            pr+=temp[i]*self.birr[i]
        if pr==x:
            for i in range(5):
                self.notes[i]-=temp[i]
            return temp
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)