# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        # 先判斷後面節點的 val
        # 如果一樣 將current 節點的指標先移到下一個
        # 刪掉中間的
        # head = 串列
        # self.current = current
        # self.first = first
        # while self.next != None :

        if head == None:
            return head
        curr = head
        while curr.next != None:
            if curr.val == curr.next.val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            else:
                curr = curr.next
        return head
        '''
        if head == None:
            return head
        curr = head
        while curr.next != None:
            if curr.val == curr.next.val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            else:
                curr = curr.next
        return head  
        '''
