from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        forward_pointer = start + 1 if start + 1 < len(nums) else None
        backward_pointer = start - 1 if start != 0 else None

        if nums[start] == target:
            return 0

        while True:
            if forward_pointer is not None:
                if nums[forward_pointer] == target:
                    return abs(forward_pointer - start)

            if backward_pointer is not None:
                if nums[backward_pointer] == target:
                    return abs(backward_pointer - start)

            forward_pointer = forward_pointer + 1 if forward_pointer + 1 < len(nums) else None
            backward_pointer = backward_pointer - 1 if backward_pointer != 0 else None



if __name__ == '__main__':
    instance = Solution()
    
    assert instance.getMinDistance(
        nums=[1, 4, 3, 7, 2, 8, 4],
        target=4, start=4,
    ) == 2

    assert instance.getMinDistance(
        nums=[3, 6],
        target=3, start=1,
    ) == 1
    