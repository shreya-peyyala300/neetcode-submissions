class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dif=set()
        for i in nums:
            if i in dif:
                return True
            dif.add(i)
        return False