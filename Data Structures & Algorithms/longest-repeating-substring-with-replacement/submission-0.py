from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        length = 0
        mapping = defaultdict(int)
        max_freq = 0

        while r < len(s):
            mapping[s[r]] += 1
            max_freq = max(max_freq, mapping[s[r]])
            r += 1

            while r - l - max_freq > k:
                mapping[s[l]] -= 1
                l += 1
            
            length = max(length, r - l)

        return length