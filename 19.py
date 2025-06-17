# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # prev = dummy 
        # current = head   
        # nextNode = head.next
        # count = 0
        # # head = [1,2,3,4] n =3
        # while current:
        #     if count == n:
        #         prev.next = current.next
        #         current = nextNode
        #         nextNode = current.next
        #     prev = current
        #     current= current.next
        #     nextNode = current.next
        
        # return dummy.next

        dummy = ListNode()
        prev = dummy
        current = head

        # set the current node at where item should replaced
        while n > 0:
            current = current.next
            n -= 1
        
        #
        while current:
            prev = 


        