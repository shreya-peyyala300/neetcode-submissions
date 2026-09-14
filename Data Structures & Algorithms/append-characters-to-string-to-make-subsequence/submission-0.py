class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j=0
        leg=len(t)
        for i in range(len(s)):
            if j< len(t)and t[j]==s[i]:
                j+=1
        return leg-j
        
