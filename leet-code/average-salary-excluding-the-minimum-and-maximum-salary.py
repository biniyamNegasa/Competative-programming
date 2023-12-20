class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum_excluded = sum(salary) - salary[0] - salary[-1]
        size = len(salary)-2
        return sum_excluded/size