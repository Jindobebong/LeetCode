class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1

        sum = ""
        remember = 0

        while i >= 0 and j >= 0:
            c = int(a[i]) + int(b[j]) + remember
            if c >= 2:
                remember = 1
            else:
                remember = 0
            sum += str(c % 2)
            i -= 1
            j -= 1
        
        while i >= 0:
            c = int(a[i]) + remember
            if c >= 2:
                remember = 1
            else:
                remember = 0
            sum += str(c % 2)
            i -= 1
        
        while j >= 0:
            c = int(b[j]) + remember
            if c >= 2:
                remember = 1
            else:
                remember = 0
            sum += str(c % 2)
            j -= 1

        if remember:
            sum += str(remember)
        sum = sum[::-1]
        return sum
    

# a = input()
# b = input()

# print(Solution.addBinary("", a, b))