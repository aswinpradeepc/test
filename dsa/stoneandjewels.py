class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(J.count, S))
