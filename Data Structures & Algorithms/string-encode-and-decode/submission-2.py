class Solution:

    def encode(self, strs: List[str]) -> str:

        null_byte = "\x00"
        rv = ""

        for s in strs:
            rv += s
            rv += null_byte

        return rv

    def decode(self, s: str) -> List[str]:

        rv = []

        index = 0

        while index < len(s):
            count = index
            curr_word = ""
            while count < len(s):
                if s[count] == "\x00":
                    break
                else:
                    curr_word += s[count]
                    count += 1
            index = count + 1
            rv.append(curr_word) 
            
        return rv