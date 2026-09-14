class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        coutn=0
        for i in range(k):
            if blocks[i]=='W':
                coutn+=1
        res=coutn
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                coutn-=1
            if blocks[i]=='W':
                coutn+=1
            res=min(res,coutn)
        return res