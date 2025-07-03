class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break
        cnt = 0
        for i in range(i, -1, -1):
            if s[i] == " ":
                break
            else:
                cnt += 1
        return cnt

s = input()
print(Solution.lengthOfLastWord(" ", s))