class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        for i in range(len(digits)-1, -1, -1):
            if digits[i]<10:
                return digits
            val=digits[i]//10
            digits[i]%=10
            if i>0:
                digits[i-1]+=val
            else:
                digits.insert(i, val)
        return digits