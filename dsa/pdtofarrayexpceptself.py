class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rrp =1
        rp = []
        lp = []
        llp = 1
        for i in range(0,len(nums)):
            rrp = rrp*nums[i]
            rp.append(rrp)
            llp = llp*nums[-i-1]
            lp.append(llp)
        lp.reverse()
        lp.append(1)
        rp.insert(0,1)
        res =[]
        for i in range(0,len(nums)):
            res.append(rp[i]*lp[i+1])
        return res