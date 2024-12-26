class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num = set(nums)
        l = n//2
        for i in num:
            if nums.count(i)>(l):
                return i
        