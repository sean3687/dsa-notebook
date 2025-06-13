# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Finding middle part of the list
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverses the second half 
        second = slow.next
        prev = slow.next = None

        while second: # Continue until second return null
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #  Finally merge two different linkedlist
        first, second = head,prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1,tmp2
