class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = {}
        for i in range(len(magazine)):
            dict_mag[magazine[i]] = dict_mag.get(magazine[i], 0) + 1
        dict_ran = {}
        for i in range(len(ransomNote)):
            dict_ran[ransomNote[i]] = dict_ran.get(ransomNote[i], 0) + 1

        for i in range(len(ransomNote)):
            # print(dict_ran[ransomNote[i]], dict_mag[magazine[i]])
            if dict_ran[ransomNote[i]] > dict_mag.get(ransomNote[i], 0):
                return False
        return True
    

sol = Solution()
print(sol.canConstruct("a", "b"))