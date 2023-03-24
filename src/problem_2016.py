from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        i = 0
        max_difference = 0
        while i < len(nums) - 1:

            j = i + 1

            while j < len(nums):

                if nums[i] < nums[j] and nums[j] - nums[i] > max_difference:
                    max_difference = nums[j] - nums[i]

                j += 1
            
            i += 1

        return max_difference if max_difference != 0 else -1



"""
[9,4,3,2]

i = 2
j = 4
max_diff = 0

"""

if __name__ == "__main__":
    nums = [7,1,5,4]

    solution = Solution()
    maximum_diff = solution.maximumDifference(nums)

    assert maximum_diff == 4


    nums = [9,4,3,2]
    solution = Solution()
    maximum_diff = solution.maximumDifference(nums)

    assert maximum_diff == -1

    nums = [1,5,2,10]
    solution = Solution()
    maximum_diff = solution.maximumDifference(nums)

    assert maximum_diff == 9
