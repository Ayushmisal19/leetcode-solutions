# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_1 = []
        current = head
        while current is not None:
            list_1.append(current.val)
            current = current.next
        index = len(list_1) - n
        list_1.pop(index)
        if len(list_1) == 0:
            return None
        head = ListNode(list_1[0])
        current = head
        for i in range(1,len(list_1)):
            new_node = ListNode(list_1[i])
            current.next = new_node
            current = current.next
        return head