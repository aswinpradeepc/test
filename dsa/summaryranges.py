class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res =[]
        first = None
        for i in range(0,len(nums)):
            if first == None:
                first = nums[i]
            if i == len(nums)-1 or nums[i]+1!=nums[i+1]:
                if first == nums[i]:
                    res.append(str(first))
                    first=None
                else:
                    res.append(str(first)+"->"+str(nums[i]))
                    first = None
        return re