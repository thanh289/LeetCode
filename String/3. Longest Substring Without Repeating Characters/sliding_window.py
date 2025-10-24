class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        result = 1
        left, right = 0, 1
        dict = {}
        while right < len(s):
            if s[right] in s[left:right]:
                if s[right] in dict:
                    left = dict[s[right]] + 1
                else:
                    left += 1              
            else:
                result = max(result, right-left+1)
            dict[s[right]] = right
            right += 1


        return result
    
sol = Solution()
print(sol.lengthOfLongestSubstring("aabaab!bb"))
        