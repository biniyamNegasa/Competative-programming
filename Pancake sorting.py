class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        a=[]
        for i in range(len(arr),1,-1):
            ind=arr.index(i)
            if ind==i-1:
                continue
            if ind!=0:
                a.append(ind+1)
                arr[:ind+1]=arr[:ind+1][::-1]
            a.append(i)
            arr[:i]=arr[:i][::-1]
        return a
