# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        cur = head
        idx = 0
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        remove_id = len(nodes) - n

        if remove_id == 0:
            return head.next
        
        nodes[remove_id - 1].next = nodes[remove_id].next

        return head

