#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # I want to remove duplicates
        # Another two pointer technique?
        '''
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            if prev.val == curr.val:
                # I want to point to the previous to the current next node
                prev.next = curr.next
            else:
                prev = curr
            # Update the current node
            curr = curr.next

        # I want it to return somehow
        # edge case
        # [0, 0, 0, 0, 0]
        # [0] should be returned
        # I should never remove the head, but remove the duplicates that come after
        return head
        '''
        curr = head
        # Two loops
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next

        return head







        
# @lc code=end

