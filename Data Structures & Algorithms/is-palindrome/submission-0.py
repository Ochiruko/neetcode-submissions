class Solution:
    def isPalindrome(self, s: str) -> bool:
        sf = "".join(filter(str.isalnum, s.lower()))
        left = 0
        right = len(sf) - 1
        while left < right:
            if sf[left] != sf[right]:
                return False
            left += 1
            right -= 1
        return True