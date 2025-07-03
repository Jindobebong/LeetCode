class Solution(object):
    def isPalindrome(self, s):
        if s == "":
            return True
        filtered = []
        for c in s:
            if c.isalnum():
                filtered.append(c.lower())

        i = 0
        j = len(filtered) - 1
        while i <= j:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1
        return True
    
s = input()
print(Solution.isPalindrome(" ", s))