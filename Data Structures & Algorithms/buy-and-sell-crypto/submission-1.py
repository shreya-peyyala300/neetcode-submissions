class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            print("1.",maxP,sell,minBuy)
            minBuy = min(minBuy, sell)
            print("2.",minBuy)
        return maxP