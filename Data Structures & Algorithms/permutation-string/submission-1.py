from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        mapping_s1 = defaultdict(int)
        for char in s1:
            mapping_s1[char] += 1
        
        l = 0
        r = 0

        mapping_s2 = defaultdict(int)
        while r < len(s2):
            if r - l < len(s1):
                mapping_s2[s2[r]] += 1
                r += 1

            else:
                if mapping_s1 == mapping_s2:
                    return True
                
                mapping_s2[s2[l]] -= 1
                if mapping_s2[s2[l]] == 0:
                    mapping_s2.pop(s2[l], None)
                mapping_s2[s2[r]] += 1
                
                l += 1
                r += 1
        
        if mapping_s1 == mapping_s2:
            return True
        return False