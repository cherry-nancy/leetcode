class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1 , 1, -1):
	        if(nums[i]==nums[i-1]==nums[i-2]):
		        del(nums[i])
        return(len(nums))
    
# Backward traversal and deletion
# TC: O(n2) -- the loop takes O(n), but each deletion can take O(n) because subsequent 
# elements must be shifted. In the worst case, there are O(n) deletions.
# Space complexity: O(1) -- no additional data structure is created.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 1
        
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[i] = nums[j]
                i += 1
                
        return i 
# Two pointers with a counter
# TC: O(N) - we traverse the array once, and each assignment takes O(1) time.
# SC: O(1) - we only use three variables, regardless of the input size.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i
# TC: O(n)
# SC: O(1)