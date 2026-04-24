class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt={}
        for i,n in enumerate(nums):
            dif=target-n
            if dif in dictt:
                return [dictt[dif],i]
            dictt[n]=i
