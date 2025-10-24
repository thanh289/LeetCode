from typing import Counter, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked = set()
        ans = []
        for i, x in enumerate(strs):
            if i in checked:
                continue
            temp = [x]
            checked.add(i)
            for j in range(i+1, len(strs)):
                if j in checked:
                    continue
                if Counter(x) == Counter(strs[j]):
                    temp.append(strs[j])
                    checked.add(j)

            ans.append(temp)
        return ans
    

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# time limit

