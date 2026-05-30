class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(n):
            for i in range(len(n)):
                if(n[i] != n[len(n)-i-1]):
                    return False
            return True
        for i in range(len(s)):
            if(s[i] != s[len(s)-i-1]):
                left = s[:i]+s[i+1:]
                right = s[:len(s)-i-1]+s[len(s)-i:]
                print(left)
                print(right)
                return ispalindrome(left) or ispalindrome(right)
        return True
        