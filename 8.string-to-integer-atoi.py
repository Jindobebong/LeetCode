class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        sum = 0

        while i < n and s[i] == ' ':
            i += 1
            
        if i >= n:
            return 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < n and s[i].isdigit():
            sum = sum * 10 + int(s[i])
            i += 1
        
        sum *= sign
        if sum < -2 ** 31:
            sum = -2 ** 31
        elif sum > 2 ** 31 - 1:
            sum = 2 ** 31 - 1
        return sum

# s = input()
# print(Solution.myAtoi("", s))






        