class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        corS,corT={},{}
        for i in range(len(s)):
            corS[s[i]]=1+corS.get(s[i],0)
            corT[t[i]]=1+corT.get(t[i],0)

        return corS==corT