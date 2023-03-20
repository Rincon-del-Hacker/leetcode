from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        if original in nums:
            return self.findFinalValue(nums, original*2)     
        
        return original


nums = [2,7,9]
original = 4


if __name__ == "__main__":
    instance = Solution()

    assert instance.findFinalValue(
        nums, 
        original
    ) == 4
