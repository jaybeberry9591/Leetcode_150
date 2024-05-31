# beats 78.59%  
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return len(x[-1])
