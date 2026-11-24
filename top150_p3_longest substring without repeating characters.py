class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ''
        maxLen = 0
        for char in s:
            if char not in tempStr:
                tempStr += char
                maxLen = max(maxLen, len(tempStr))                                
            else:
                tempStr ='' + tempStr[tempStr.index(char)+1:] + char

        return maxLen

#TC: O(NM)
# Logic: sliding window approach, 
# for each character char in s: if char is not in the window, append it to tempStr and update maxLen if the window
# is now the logest seen so far.
# char is already in the window. The window must shrink so the duplicate disappears. Find the earlier occurrence
# with tempStr.index(char), drop everything up to it and including it, and append the new char. 
# TC: O(n.k): n is the length of s and k is the size of the character set. In the worst case, 
#  we might have to scan through the entire tempStr to find the index of char, which can take O(k) time.
# space: O(min(n,k)), for the tempStr window, which holds only unique characters.





#below use hash table, O(n)
def lengthOfLongestSubstring(self, s: str) -> int:
    last = {}
    left = maxLen = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        maxLen = max(maxLen, right - left + 1)
    return maxLen

# Also a sliding window logic, but instead of storing the window as a string, it stores it as two indices:
# left and right. The window is s[left..right], and the invariant is that it never contains a repeated character.
# Time complexity: O(n)
# The loop runs once over the string (n iterations).
# Each iteration does only dictionary lookups, assignments, and arithmetic, all O(1) on average.
# left never moves backward and jumps forward, so there is no re-scanning of characters.
# Space: O(min(n,k)) 
# last holds one entry per distinct character, so its size is bounded by both the string length n and 
# the alphabet size k.
# everything else (left, right, maxLen) is O(1).




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_length = 0
        window = Counter()
        while (right < len(s)):
            window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -=1
                left +=1

            max_length = max(max_length, right - left +1)
            right += 1

        return max_length
