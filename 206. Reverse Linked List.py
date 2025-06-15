# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        store_next = head.next
        head.next = None
        curr = head
        while curr:
            prev = curr
            curr = store_next
            if not curr:
                break
            store_next = curr.next
            curr.next = prev
        head = prev
        return head
