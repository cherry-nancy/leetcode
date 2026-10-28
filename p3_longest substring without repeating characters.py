 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ''
        maxLen = 0
        for char in s:
            if char not in tempStr:
                tempStr += char
                maxLen = max(maxLen, len(tempStr))
            else:
                if tempStr[-1] == char:
                    tempStr = '' + char                                       
                else:
                    tempStr ='' + tempStr[tempStr.index(char)+1:] + char
        return maxLen

#TC: O(NM)

#below use hash table, O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        p1 = 0
        d = {}
        for p2 in range(len(s)):
            if s[p2] in d:
                p1 = max(p1, d[s[p2]]+1)
            ans = max(ans, p2 - p1 + 1)
            d[s[p2]] = p2

        return ans


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
