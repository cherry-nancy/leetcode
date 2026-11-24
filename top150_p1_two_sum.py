
#p1: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

 class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner not in d:
                d[num] = i
            else:
                return [d[partner], i]
        
        
#time complexity o(n), space complexity o(n)
# Time complexity describes how the number of operations in an algorithm increases as the size of the input increases. 
# Space complexity describes how the amount of memory used by an algorithm increases as the size of the input increases.

# Neither measures actual seconds or bytes. 
# They tell you how the cost scales: if the input doubles, does the work double (O(n)), quadruple (O(n²)), or barely change (O(1))?
# Common growth rates, from fastest to slowest: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ).

#Applying it to your code

# Time: O(n). The for loop runs at most n times. Inside it, partner not in d, d[num] = i, and d[partner] are dictionary operations, 
# which are O(1) on average thanks to hashing. So you do O(1) work, n times, giving O(n).

# Compare with the brute force approach (check every pair with nested loops), which is O(n²). 
# The dictionary trades memory for speed.

# Space: O(n). In the worst case (no pair found until the end, or never), the dict d stores every element, 
# so it holds up to n entries. Everything else (i, num, partner) is O(1).


#sort first then two pointers

class Solution(object):
   def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        numbers = [(number, index) for index, number in enumerate(nums)]
        numbers.sort()  # sorts the list in place and returns None
        
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left][0] + numbers[right][0] > target:
                right -= 1
            elif numbers[left][0] + numbers[right][0] < target:
                left += 1
            else:
                return sorted([numbers[left][1], numbers[right][1]])  # leaves the orginal alone and returns a new sorted list.
            
        return [-1, -1]






#p2: lintcode 608 two sum II input array is sorted

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

#two pointers, TC O(n), SC: O(1)

#P3: lintcode 607 Two sum III - Data structure design

class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing

    def add(self, number):
        self.count[number] = self.count.get(number, 0) + 1


    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False

