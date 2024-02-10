#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Imagine if I could use two pointers
        # Traversing through nodes
        '''
        # Array Solution
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
        '''
        fast = head
        slow = head
         
        # While fast is not null
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the 2nd half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev 
            prev = slow
            slow = tmp

        # Check the palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True




# @lc code=end

