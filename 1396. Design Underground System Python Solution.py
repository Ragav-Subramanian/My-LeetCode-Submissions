class UndergroundSystem:

    def __init__(self):
        self.sum={}
        self.start={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        v=self.start[id]
        if (v[0],stationName) not in self.sum:
            self.sum[(v[0],stationName)]=[0,0]
        self.sum[(v[0],stationName)][0]+=(t-v[1])
        self.sum[(v[0],stationName)][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.sum[(startStation,endStation)][0]/self.sum[(startStation,endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)