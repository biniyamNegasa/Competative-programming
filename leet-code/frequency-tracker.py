class FrequencyTracker:

    def __init__(self):
        self.dic=defaultdict(int)
        self.fr=defaultdict(int)

    def add(self, number: int) -> None:
        if self.fr[self.dic[number]]>1:
            self.fr[self.dic[number]]-=1
        elif self.fr[self.dic[number]]==1:
            self.fr.pop(self.dic[number])
        self.dic[number]+=1
        self.fr[self.dic[number]]+=1
        
    def deleteOne(self, number: int) -> None:
        if number in self.dic:
            if self.fr[self.dic[number]]>1:
                self.fr[self.dic[number]]-=1
            elif self.fr[self.dic[number]]==1:
                self.fr.pop(self.dic[number])
            if self.dic[number]>1:
                self.dic[number]-=1
            elif self.dic[number]==1:
                self.dic.pop(number)
            self.fr[self.dic[number]]+=1
        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.fr


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)