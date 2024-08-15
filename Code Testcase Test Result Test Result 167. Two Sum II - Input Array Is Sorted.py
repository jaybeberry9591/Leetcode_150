class Solution:

    def binary_search(self,numbers,key,low,high):
        while low <= high:
            mid = int ((low+high)/2)
            if key == numbers[mid]:
                return mid
            elif numbers[mid]>key:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        

        for i in range(len(numbers)):
            key = target - numbers[i]
            left = i + 1
            result = self.binary_search(numbers, key, left, right)
            if result != -1:
                return [i + 1, result + 1]


        
        return []
