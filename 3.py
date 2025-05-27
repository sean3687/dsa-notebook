class Solution:
    def lengthOfLongestSubstring(self, s:str):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res, r-1+1)
        return res
