class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        x=capacity
        for i,num in enumerate(plants):
            if num<=x:
                x-=num
                ans+= 1
            else:
                x=capacity
                x-=num
                ans+=2*i+1
        return ans