from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            print("1",prefix)
            prefix *= nums[i]
            print("res",res)
            

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            print("2",postfix)
            print("res2",res)

        return res