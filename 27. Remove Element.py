class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        track = 0
        for num in nums :
            if num != val:
                nums[track] = num
                track += 1
        return track 
