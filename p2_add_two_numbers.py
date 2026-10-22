
Linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = ListNode(0)  # dummy head
        ptr = result  # ptr is the tail pointer: it always points at the last node built so far.
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)   
            #The divmod() method takes two numbers and returns a pair of numbers(a tuple)
            #consisting of their quotient（商） and remainder.
                      
            ptr.next = ListNode(out)
            ptr = ptr.next   # reassignment of the name ptr.                   
            
            l1 = l1.next if l1 else None  #不能是l1.next
            l2 = l2.next if l2 else None
               
        return result.next
    
    # ctrl + l to comment out multiple lines of code

#TC O(max(m,n)), assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m, n) times.
# SC: O(max(m,n)). The length of the new list is at most max(m, n) + 1.
# #########################################################################
# The key idea: result and ptr are two names pointing at nodes, and ptr is the “cursor” that walks forward while result 
# stays put so you can return the head at the end.

#The setup
# python
# result = ListNode(0)
# ptr = result

# This creates one node (value 0) and makes both result and ptr refer to the same node. No copy happens. Think of them as two sticky notes on one object.

# result is a dummy head. Its value (0) is never used. It exists so you don’t have to write special code for “the first node of the answer.”
# ptr is the tail pointer: it always points at the last node built so far.
# ptr.next = ListNode(out)

# This creates a new node holding the digit out and links it onto the end of the list by setting the current tail’s next field. Notice this modifies the node that ptr points to, so result (pointing at the same first node) also “sees” the new node via result.next.

# ptr = ptr.next

# This is a reassignment of the name ptr, not a modification of any node. It moves the cursor forward onto the node you just added, so the next iteration appends after it. result is not affected and still points at the dummy head.

# Walkthrough: 2→4 plus 5→6 (i.e. 42 + 65 = 107, digits stored reversed: 7→0→1)

# Start: result → [0], ptr → [0] (same node)

# Iteration 1: 2 + 5 = 7, so carry=0, out=7

# ptr.next = ListNode(7)     result → [0] → [7]
# ptr = ptr.next             ptr is now on [7]

# Iteration 2: 4 + 6 = 10, so carry=1, out=0

# ptr.next = ListNode(0)     result → [0] → [7] → [0]
# ptr = ptr.next             ptr is now on the second node, [0]

# Iteration 3: both lists exhausted, but carry=1, so the loop still runs (that’s why or carry is in the condition). out=1, carry=0

# ptr.next = ListNode(1)     result → [0] → [7] → [0] → [1]
# ptr = ptr.next

# Loop ends. ptr is at the last node, but result still points at the dummy head, so:

# python
# return result.next     # skips the dummy 0, returns 7 → 0 → 1
# Why result.next and not ptr?

# By the end, ptr points at the tail, so returning it would give only the last digit. result is the only handle that still leads to the whole chain, and .next skips the throwaway dummy node.

# About your note on l1.next

# You’re right. If l1 is None, then l1.next raises an AttributeError, because None has no .next. That’s why you need l1.next if l1 else None. One list may be shorter than the other, so it can run out first while the other keeps going.

# Complexity

# Time is O(max(m, n)), where m and n are the list lengths, since you visit each position once. Space is O(max(m, n)) for the output 
# list (O(1) if you don’t count the output).

# why can result.next sees ptr.next? Because result and ptr are two names pointing at the same node. 
# When you do ptr.next = ListNode(out), you modify the node that both names refer to, so result.next also sees the new node.
# you can verify if they are the same object by running : result = ListNode(0) ptr = result