# it beats 75.76 %

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = False

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                ans = i
                flag = True
                break
                
        if flag == False :
            ans = -1

            
        return ans
