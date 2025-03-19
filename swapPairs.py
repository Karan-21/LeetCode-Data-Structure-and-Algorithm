# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://www.youtube.com/watch?v=bM2kxaTUwGw
class Solution:
	def swapPairs(self, head: ListNode) -> ListNode:

		if not head or not head.next:
			return head
		
		tmp = head
		head = head.next
		tmp.next = head.next
		head.next = tmp
		
		tmp.next = self.swapPairs(tmp.next)
		
		return head 
        
