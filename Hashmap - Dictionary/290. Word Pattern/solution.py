class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}

        pattern_list = list(pattern)
        s_list = s.split(' ')
        if len(pattern_list) != len(s_list):
            return False
        
        pattern_set = set(pattern_list)
        s_set = set(s_list)
        if len(pattern_set) != len(s_set):
            return False


        for i in range(len(pattern)):
            if dict.get(pattern[i], '') != '':
                if dict[pattern[i]] != s_list[i] :
                    return False
            else:
                dict[pattern[i]] = s_list[i]
        return True
    
sol = Solution()
print(sol.wordPattern("abba", "dog dog dog dog"))
