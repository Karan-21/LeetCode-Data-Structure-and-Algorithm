# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://www.youtube.com/watch?v=UcGtPs2LE_c
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        # Finding the Length of LinkedIn List
        n = 1
        temp = head
        while temp.next:
            temp = temp.next
            n+=1
        
        # After N rotation it will come back to Same List
        # If K is out of Bound => Bring in to our N's Range
        k = k % n

        # If there is No Rotation => Returns the Same LinkedIn List
        if k == 0:
            return head
        
        # Go to the element just before we want to split it
        curr = head    
        for i in range(n-k-1):
            curr = curr.next
        
        # Get the New Head from element.next we have traversed
        newHead = curr.next

        # Split the LL by pointing it to NULL
        curr.next = None

        # Now Point the Last Node to the Head
        temp.next = head

        # Finally, Return the NewHead
        return newHead

# n - k - 1 = 5 - 2 - 1 = 2

#              curr            newHead     
#         1, 2, 3 -> NULL        4, 5
#                                  temp
        
#         4 -> 5 -> 1 -> 2 -> 3 -> NULL
