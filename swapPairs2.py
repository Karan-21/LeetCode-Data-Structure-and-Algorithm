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
