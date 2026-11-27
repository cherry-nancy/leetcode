#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#The number of elements initialized in nums1 and nums2 are m and n respectively. 
#You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from 
#nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

#TC: O(n+m)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
                
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# TC: O(n+m), 
# SC:O(1) : only three additional variables, p1, p2 and p.
# Why is the second while loop necessary?
# Because if nums2 is exhausted first, the remaining elements in nums1 are already in place, so no more work is 
# needed.
# if nums1 is exhausted first, we need to copy over the numbers from nums2 into nums1.