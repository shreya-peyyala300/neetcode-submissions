class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hat=set()
        for i in nums:
            if i in hat:
                return True
            hat.add(i)
        return False