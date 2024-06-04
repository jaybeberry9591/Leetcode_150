class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        length = len(result)

        for i in range(1,len(strs)):
            while strs[i].find(result)!=0:
                result = result[:length-1]
                length = length - 1

                if not result:
                    return ""

        return result   
