class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff_fw = [0]
        diff_bw = [0]
        for i in range(1, n):
            diff_fw.append(diff_fw[-1]+(nums[i]-nums[i-1]))
        for i in range(1, n):
            diff_bw.append(nums[i]-nums[i-1])
        fw_sum = sum(diff_fw)
        bw_sum = 0
        ans = []
        for i in range(n):
            bw_sum += i*diff_bw[i]
            fw_sum -= (n-i)*diff_bw[i]
            ans.append(fw_sum + bw_sum)
        return ans