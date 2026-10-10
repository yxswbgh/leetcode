# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1: #新建链表来反转
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur=None #当前节点
        while head!=None:
            new_node=ListNode(head.val,None)
            new_node.next=cur

            cur=new_node

            head=head.next
        return cur

class Solution2: #原地反转
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre=None

        while head!=None:
            next_node=head.next

            head.next=pre

            pre=head
            head=next_node
            #next_node=head.next

        return pre