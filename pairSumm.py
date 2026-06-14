# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=fast
        rev=None
        while fast:
            fast=fast.next.next
            nextNode=slow.next
            slow.next=rev
            rev=slow
            slow=nextNode
        ans=0
        while slow:
            ans=max(ans, rev.val+slow.val)
            rev=rev.next
            slow=slow.next
        return ans
