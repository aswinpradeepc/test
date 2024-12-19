class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hp=0
        minBuy = prices[0]
        for i in range(0,len(prices)):
            minBuy = min(minBuy, prices[i])
            lp = prices[i]-minBuy
            if lp>hp:
                hp = lp
        return hp
            