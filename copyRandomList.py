"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None: None}

        temp = head

        while temp:

            newNode = Node(temp.val)

            oldToNew[temp] = newNode
        
            temp = temp.next
        
        temp = head

        while temp:

            curr = oldToNew[temp]

            curr.next = oldToNew[temp.next]

            curr.random = oldToNew[temp.random]

            temp = temp.next
        
        return oldToNew[head]
