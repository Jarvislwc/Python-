# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):

        prev = None

        # if head == None:
        #   return head
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
