class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        no=len(nums)
        n=[0]*(2*no)
        for i , num in enumerate(nums):
            n[i]=n[i+no]=nums[i]
        return n