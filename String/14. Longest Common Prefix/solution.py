from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        str0 = strs[0]
        min_len = min(len(x) for x in strs)
        
        for i in range(min_len):
            for x in strs:
                if str0[i] != x[i]:
                    return result
            result += str0[i]
        return result

# special case is [""]
sol =  Solution()
result = sol.longestCommonPrefix(["flower","flow","flight"])
print(result)