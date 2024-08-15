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


### two pointers solution

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # If no solution is found

