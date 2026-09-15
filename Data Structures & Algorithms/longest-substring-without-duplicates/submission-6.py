from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mapping = defaultdict()
        l = 0
        r = 0
        length = 0

        while r < len(s):
            if s[r] not in mapping:
                mapping[s[r]] = r

            else:
                index = mapping[s[r]]
                while l < index + 1:
                    if s[l] in mapping:
                        mapping.pop(s[l], None)
                    l += 1
                mapping[s[r]] = r

            r += 1
            length = max(r - l, length)
        
        
        return length