class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={f'{i}':i for i in range(10)}
        num1_int = 0
        num1_len = len(num1)-1
        for ch in num1:
            num1_int += dic[ch]*10**num1_len
            num1_len-=1
        num2_int = 0
        num2_len = len(num2)-1
        for ch in num2:
            num2_int += dic[ch]*10**num2_len
            num2_len-=1
        return f'{num1_int*num2_int}'