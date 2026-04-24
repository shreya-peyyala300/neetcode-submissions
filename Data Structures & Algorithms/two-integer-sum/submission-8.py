class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            s= target-n
            if s in dic:
                return [dic[s],i]
            dic[n]=i