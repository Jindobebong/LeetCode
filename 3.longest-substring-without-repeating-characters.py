class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi = -50005
        seen = set()
        left = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxi = max(maxi, right - left + 1)
        return maxi

s = input()
print(Solution.lengthOfLongestSubstring(" ", s))

# abcabcbb