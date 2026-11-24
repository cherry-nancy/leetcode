Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0 or k == len(nums) or k % len(nums) == 0:
            return nums
        
        k = k % len(nums)
        # Using a queue 
        # pop() last element
        q = nums #deque(nums)
        for _ in range(len(nums) - k):
            num = q.pop(0)
            q.append(num)
        
        return q