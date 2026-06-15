# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/solutions/1611982/java-python3-slow-and-fast-pointers-w-brief-explanation-and-analysis/
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return head.next
        
        slow = head

        fast = head.next.next

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next
        
        slow.next = slow.next.next

        return head
    
