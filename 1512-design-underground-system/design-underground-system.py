class UndergroundSystem:

    def __init__(self):
        self.id_to_city = {}
        self.city_to_distances = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_to_city[id] = [stationName , t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.id_to_city[id][0]
        time = self.id_to_city[id][1]
        tuples = (start_station ,stationName )
        if tuples in self.city_to_distances:
            self.city_to_distances[tuples][0] += (t - time)
            self.city_to_distances[tuples][1] += 1
        else:
            self.city_to_distances[tuples] = [t - time , 1]
        del self.id_to_city[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.city_to_distances[(startStation ,endStation)][0]/self.city_to_distances[(startStation ,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)