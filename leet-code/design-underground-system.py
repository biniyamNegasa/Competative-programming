class UndergroundSystem:

    def __init__(self):
        self.cin={}
        self.travel=defaultdict(lambda : [0,0])
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cin[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.travel[(self.cin[id][0], stationName)][0]+=t-self.cin[id][1]
        self.travel[(self.cin[id][0], stationName)][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot=self.travel[(startStation, endStation)][0]
        val=self.travel[(startStation, endStation)][1]
        return tot/val if val else 0

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)