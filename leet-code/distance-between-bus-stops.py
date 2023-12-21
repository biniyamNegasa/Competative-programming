class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            first=sum(distance[:destination])+sum(distance[start:])
            second=sum(distance[destination:start])
        else:
            first=sum(distance[start:destination])
            second=sum(distance[:start])+sum(distance[destination:])
        return min(first, second)