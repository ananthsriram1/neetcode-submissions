class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        stack = []
        
        for i in range(0, len(s) // 2):
            stack.append(s[i])

        for i in range(len(s) - (len(s) // 2), len(s)):
            comp = stack.pop()
            if s[i] != comp:
                return False

        return True