# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      list_1 = []
      current = head
      while current is not None:
        list_1.append(current.val)
        current=current.next
      new_head = None
      for i in range(len(list_1)):
        node = ListNode(list_1[i])
        node.next = new_head
        new_head = node
        
      return new_head

        