from collections import defaultdict
from typing import List


class Solution:
    # First time use this kind of dict -.-
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
    

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



