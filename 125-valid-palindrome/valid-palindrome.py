class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(c.lower() for c in s if c.isalnum()) == "".join(c.lower() for c in s if c.isalnum())[::-1]
        