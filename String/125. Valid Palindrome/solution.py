class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for i in range(len(s)):
            conv = ord(s[i])
            if(conv >= 65 and conv <= 90) \
                or (conv >= 97 and conv <= 122) \
                or (conv >= 48 and conv <= 57):
                new_str = new_str + s[i]

        return new_str == new_str[::-1]
    

# 7 ms