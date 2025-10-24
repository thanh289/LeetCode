class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s.lower()))
        return new_s == new_s[::-1]
    

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))