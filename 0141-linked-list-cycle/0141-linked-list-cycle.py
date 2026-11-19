# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_1 =set()
        current = head
        while current is not None:
            if current in list_1:
                return True
            else:
                list_1.add(current)
                current = current.next
        return False
        