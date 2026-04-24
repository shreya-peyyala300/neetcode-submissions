class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            print('r->',r)
            if s[r] in mp:
                print(s[r],r)
                l = max(mp[s[r]] + 1, l)
                print('bro:',mp[s[r]],s[r])
            mp[s[r]] = r
            print("res->>>>",res,r-l+1)
            res = max(res, r - l + 1)
        return res