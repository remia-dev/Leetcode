#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Assign head
        '''
        curr = head 
        prev = None
        while curr.next != None:
            if curr.val == val:
                curr = prev
                return curr
            prev = curr
            curr = curr.next
        '''
        # Two pointer in a linked list
        # Create a dummy node
        # Prev = dummy | points to the new head
        # curr = head
        # If curr is not equal to val
        # then shift
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            # nxt = curr.next
            if curr.val == val:
                # Remove/Shift to the next
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
        return dummy.next

        

            



        
# @lc code=end


