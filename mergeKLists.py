# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mini = []

        dummy = ListNode(0)

        temp = dummy

        for i in range(len(lists)):

            if lists[i]:

                heapq.heappush(mini, (lists[i].val, i))

                lists[i] = lists[i].next
    

        while mini:

            val, idx = heapq.heappop(mini)

            temp.next = ListNode(val)

            if lists[idx]:

                heapq.heappush(mini, (lists[idx].val, idx))

                lists[idx] = lists[idx].next
            
            temp = temp.next
        
        return dummy.next
