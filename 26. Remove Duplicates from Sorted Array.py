class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [0,0,1,1,1,2,2,3,3,4]
        prev = None
        i = 0

        for x in nums:
            if x != prev:
                nums[i] = x
                prev = x
                i += 1
                # print(nums, prev, i)
                
        return i 
