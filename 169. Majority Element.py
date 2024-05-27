# This code TLE 

# majority of elements

import math
nums = [2,2,1,1,1,2,2]

dict_nums = {}

counter = 0

for i in nums:
    counter = 0 
    for j in nums:
        if i == j:
            counter += 1
            dict_nums[i] = counter

            
# print(dict_nums)

compare = math.ceil(int((len(nums)/2))) 
# print(compare)
result = 0
for key, values in dict_nums.items():
#     print(key,values)
    if values > compare:
#         print("inside compare",values)
        result = key

return result


#######################################
#found in tutorial 
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
