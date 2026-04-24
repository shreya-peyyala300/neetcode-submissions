class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dif=defaultdict(list)
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            dif[tuple(count)].append(s)
        return list(dif.values())