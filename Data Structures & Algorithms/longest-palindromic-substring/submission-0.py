class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # odd length
            p1 = expand(i, i)
            if len(p1) > resLen:
                res = p1
                resLen = len(p1)

            # even length
            p2 = expand(i, i+1)
            if len(p2) > resLen:
                res = p2
                resLen = len(p2)

        return res