class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        x = "".join(str(x) for x in digits)
        num = int(x)+1
        str_num = str(num)

        result = [int(i) for i in str_num]

        return result
