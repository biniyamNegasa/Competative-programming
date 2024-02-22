class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zp = sorted(zip(position, speed), key=lambda x: x[0]) 
        time = [(target-p)/s for p,s in zp]
        stk = []
        for t in time:
            while stk and stk[-1]<=t:
                stk.pop()
            stk.append(t)
        return len(stk)