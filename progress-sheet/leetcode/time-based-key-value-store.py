class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ind = bisect_right(self.dic[key], timestamp, key=lambda x: x[1])-1
        if ind<0:
            return ''
        return self.dic[key][ind][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)