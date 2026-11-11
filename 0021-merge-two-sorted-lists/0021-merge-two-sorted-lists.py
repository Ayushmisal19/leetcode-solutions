# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_3 = []
    
        current = list1
        while current is not None:
            list_3.append(current.val)
            current = current.next
        current = list2
        while current is not None:
            list_3.append(current.val)
            current = current.next
        list_3 = sorted(list_3)
        if not  list_3:
            return None
        head = ListNode(list_3[0])
        Node = head
        for i in range(1,len(list_3)):
            Node_1 = ListNode(list_3[i])
            Node.next=Node_1
            Node = Node_1
        return head
        