from collections import deque

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
        q = nums # deos not create a copy of nums, essentially nums is a reference to q
        for _ in range(len(nums) - k):
            num = q.pop(0)
            q.append(num)
        
        return q
    
# TC: O(n2) because pop(0) is O(n)
# SC: O(1)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return

        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# TC: reverse the entire array O(n) + reverse the first k elements O(k) + reverse the rest O(n-k) = O(n).
# SC: o(1) -- only two pointers and a few variables are used, so the space complexity is constant.