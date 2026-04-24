class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        mpio=prices[0]
        for i in prices:
            maxp=max(maxp,i-mpio)
            mpio=min(mpio,i)
        return maxp