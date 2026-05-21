class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(c.lower() for c in s if c.isalnum())

        for i, c in enumerate(pal):
            if c != pal[len(pal) - i -1]:
                return False
        return True