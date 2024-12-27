class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = [{},]
        i = 0
        n = len(nums)
        l=[]
        nums.sort()
        numsSet = set(nums)
        for k in nums:
            if (k-1 in res[i]):
                res[i].add(k)
            else:
                i+=1
                res.append(set())
                res[i].add(k)
        print(res)
        for i in range(len(res)):
            l.append(len(res[i]))
        if len(l)>0:
            return max(l)
        else:
            return len(res[0])
        