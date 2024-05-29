# TLE on test case 34/38

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1

        for rotation in range(k):
            temp = nums[-1]
            i = 0
            n = len(nums) - 1
            while (n >= 1):
                nums[n - i] = nums [n - i-1]
                n -= 1
            nums[0] = temp

        return nums


# beats 99.09 %

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums) 
        nums[:] = nums[-n:] + nums [:-n]
        return nums
