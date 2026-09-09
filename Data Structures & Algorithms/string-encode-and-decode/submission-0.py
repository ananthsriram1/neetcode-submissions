class Solution:

    def encode(self, strs: List[str]) -> str:
        em_dash = "\u2014"
        rv = ""

        for s in strs:
            rv += s
            rv += em_dash

        return rv


    def decode(self, s: str) -> List[str]:
        rv = []
        count = 0
        curr_str = ""

        while count < len(s):
            for i in range(count, len(s)):
                if s[i] == "\u2014":
                    rv.append(curr_str)
                    curr_str = ""
                    count = i + 1
                    break

                else:
                    curr_str += s[i]

        return rv




