class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        current_sum = arr[0]  # Start with the first element
        max_sum = arr[0]      # Start with the first element

        for num in arr[1:]:  # Start iterating from the second element
            current_sum = max(num, current_sum + num)  # Either start new subarray or continue
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed
    
        return max_sum