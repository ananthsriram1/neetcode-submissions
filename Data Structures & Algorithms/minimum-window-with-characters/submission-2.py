from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        def s_contains_t(first_map, second_map):
            for key in second_map:
                if first_map[key] < second_map[key]:
                    return False
            return True

        need = Counter(t)
        have = defaultdict(int)
        need_matches = len(need)

        l = 0

        res = ""
        min_length = float('inf')

        have_matches = 0

        for r in range(len(s)):
            char = s[r]
            have[char] += 1

            if char in need and need[char] == have[char]:
                have_matches += 1

            while have_matches == need_matches:
                if (r - l + 1) < min_length:
                    res = s[l : r + 1]
                    min_length = (r - l + 1)

                left_char = s[l]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    have_matches -= 1

                l += 1

        return res