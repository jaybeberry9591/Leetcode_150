# beats 5.05 %

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0 or len(magazine) == 0 or len(ransomNote) > len(magazine):
            return False

        freq_ransomNote = {}
        freq_magazine = {}
        for items in ransomNote:
            freq_ransomNote[items] = ransomNote.count(items)

        for items in magazine:
            freq_magazine[items] = magazine.count(items)

        # print(freq_ransomNote, freq_magazine)
        flag = 0
        for i in freq_ransomNote:
            if freq_magazine.get(i) == None or freq_ransomNote[i] > freq_magazine.get(i) :
                flag = 1
                break
        if flag == 0: 
            return True
        else:
            return False
        
