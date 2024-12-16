class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =''
        n = min(len(word1),len(word2))
        for i in range (0,n):
            result= result+word1[i]+word2[i]
        if len(word1)==len(word2):
            return result
        elif len(word1)>len(word2):
            return result+word1[n:]
        else:
            return result+word2[n:]
            
        