class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        for bill in bills:
            dic[bill]+=1
            val = bill-5
            if val//10<=dic[10]:
                dic[10]-= val//10
                val%=10
            if val//5<=dic[5]:
                dic[5]-= val//5
                val%=5
            else:
                return False
        return True
            