class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            si = "".join(sorted(i))
            d[si].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res

