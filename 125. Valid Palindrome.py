import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.split()
        my_string = "".join(x)
        clean_text = re.sub(r'[^A-Za-z0-9]+', '', my_string)
        reverse_text =  clean_text[::-1]

        if clean_text.lower() == reverse_text.lower():
            return True
        else:
            return False
