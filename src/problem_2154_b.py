from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original *= 2
        
        return original

nums = [2,7,9]
original = 4


if __name__ == "__main__":
    instance = Solution()

    assert instance.findFinalValue(
        nums, 
        original
    ) == 4
