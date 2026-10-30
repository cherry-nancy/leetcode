
>>> #Longest palindrome substring
#中心线枚举
class Solution:
    def longestPalindrom(self, s):
        if not s:  #s is None, or s =""
            return ""
        
        start, longest = 0, 0
        for middle in range(len(s)):
            # odd
            left, right = middle, middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left - 1:   # pay attention, here it is - 1
                longest = right - left -1
                start = left + 1
            # even
            left, right = middle, middle + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left - 1:  # pay attention, here it is - 1
                longest = right - left - 1
                start = left + 1
                
        return s[start:start + longest]
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        start, longest = 0, 1

        def expand(left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1  # (start, length)

        for i in range(n):
            # No remaining center can beat the current best
            if longest >= 2 * (n - i):
                break
            for l, r in ((i, i), (i, i + 1)):  # odd, even
                st, ln = expand(l, r)
                if ln > longest:
                    start, longest = st, ln

        return s[start:start + longest]


class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrome_from(s, mid, mid))
            answer = max(answer, self.get_palindrome_from(s, mid, mid + 1))
        return s[answer[1]: answer[0] + answer[1]]
        
    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        return right - left - 1, left + 1

#time complexity O(n^2)
#steps: for every character, uses it as center and then uses two pointers left and right to spread
#           also uses abba format to spread, return the length, and starting postion 


>>> #dynamic programming
def longestPalindrom(s):
    if not s:
        return ""
    
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True
    for i in range(1, n):
        is_palindrome[i][i - 1] = True #if comment this out, then can't handle even cases
        
    start, longest = 0, 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
            if is_palindrome[i][j] and length > longest:
                longest = length
                start = i
    
    return s[start:start + longest]