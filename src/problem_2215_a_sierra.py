from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = self.substraction(nums1, nums2)
        set_2 = self.substraction(nums2, nums1)
        return [list(set_1), list(set_2)]

    def substraction(self, my_list: List[int], compared: List[int]):
        my_set = set()
        for item in my_list:
            if item not in compared:
                my_set.add(item)

        return my_set


if __name__ == '__main__':
    solution = Solution()

    nums1 = [1,2,3]
    nums2 = [2,4,6]
    find_difference = solution.findDifference(nums1, nums2)
    assert find_difference == [[1,3],[4,6]]

    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    find_difference = solution.findDifference(nums1, nums2)
    assert find_difference == [[3],[]]
    