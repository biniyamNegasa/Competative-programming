class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        mx_lst = []
        for i in range(0, len(tasks), 4):
            mx_lst.append(processorTime[i//4]+max(tasks[i:i+4]))
        return max(mx_lst)