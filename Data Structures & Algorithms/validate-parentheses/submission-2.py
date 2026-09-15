class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {}
        mapping["("] = ")"
        mapping["["] = "]"
        mapping["{"] = "}"

        stack = []

        for i in range(len(s)):
            
            if s[i] in mapping:
                stack.append(s[i])
            else:
                if len(stack) <= 0:
                    return False
                comp = stack.pop()
                if s[i] != mapping[comp]:
                    return False

        if len(stack) > 0:
            return False
        return True