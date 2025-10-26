from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        result = ''
        for i in range(len(s)):
            result  = result + s[i]
        return result
    
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))