class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        coun=[0]*26
        for i in range(len(s)):
            coun[ord(s[i])-ord('a')]+=1
            coun[ord(t[i])-ord('a')]-=1
        for val in coun:
            if val!=0:
                return False
        return True