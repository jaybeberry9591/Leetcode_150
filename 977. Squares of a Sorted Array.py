class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = list(map(lambda x: x ** 2, nums))
        nums2.sort()
        return nums2
        
