#################################################################################
# Given an integer array nums and an integer val, remove all occurrences of val 
# in nums in-place. The order of the elements may be changed. Then return the number 
# of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are 
# not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
###############################################################################################
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] == val:
                continue
            else:
                nums[i] = nums[j]
                i += 1                
        return i 
# TC: O(n), for loop executes exactly n times, others are all o(1) operations.
# SC: O(1), only two variables are used.



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j <len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
# TC and SC are same as above. For loop is generally preferable for readability.