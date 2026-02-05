class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # idea frequency of elements from ransomNote
        # I used two hashmaps but I can just use one counter for magazine
        # and iterate over ransomNote and If I find that character in 
        # ransomNote, i decrement the count for that particular ch

        m_count = {}
        for ch in magazine:
            m_count[ch] = m_count.get(ch, 0) + 1 

        for ch in ransomNote:
            if key in m_count and m_count[key] > 0:
                m_count[key] -= 1
            else:
                return False
        return True

assert Solution().canConstruct(ransomNote = "a", magazine = "b") == False
assert Solution().canConstruct(ransomNote = "aa", magazine = "ab") == False
assert Solution().canConstruct(ransomNote = "aa", magazine = "aab") == True

