from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # valor -> índice
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            if complemento in seen:
                return [seen[complemento], i]
            
            seen[num] = i


nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))