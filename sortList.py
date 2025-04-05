# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        slow = fast = head

        temp = None

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
    
        return self.solve(l1,l2)
    
    def solve(self,l1,l2):

        dummy = ListNode(0)

        temp = dummy

        while l1 and l2:

            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        
        if l1:
            temp.next = l1
        
        if l2:
            temp.next = l2
        
        return dummy.next
