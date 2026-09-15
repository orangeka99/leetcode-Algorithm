# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h_length = head
        length = 0
        if not head:
            return None
        while h_length:
            length += 1
            h_length = h_length.next
        if length == 1:
            return None
        current = head
        target = length - n
        if target == 0:
            return head.next
        length = 0

        while current and current.next:
            length += 1
            if length == target:
                current.next = current.next.next
                break
            else:
                current = current.next
        return head
        
            
        
        
        
        
        
        




