class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]

##
# improved Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            k = target-nums[i]
            nums[i] = "a"
            if k in nums:
                j = nums.index(k)
                return [i, j]