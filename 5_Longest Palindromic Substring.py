class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ""
        for i in range(0, len(s)):
            for j in range(len(s), i, -1):
                if len(temp) >= j - i:
                    # print(len(temp))
                    break
                elif s[i:j] == s[i:j][::-1]:
                    # elif s[i:j]==s[i:j:-1]:
                    # print("i: ",i)
                    # print("j: ",i)
                    # print(s[i:j][::-1])
                    temp = s[i:j]
                    continue
        if len(s) == 1:
            temp = s

        return temp

