# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: 
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        #题目要求原地拼接两个链表，不能新建
        #⭐虚拟头节点，处理初始化（不知道头节点是谁，头节点可能被删掉，从0建一个链表）

        '''
        #以下是麻烦方法，用两个指针指向最终链表的头尾
        head=None
        cur=None
        while True:
            if list1.val<=list2.val:
                head=list1
                cur=list1
                list1=list1.next
            else:
                pass

        #第一次可以，但后面循环没法写
        #要在while之前写一个if else判断谁是头节点，代码很冗余
        '''

        #经验来说，初始化为None边界很难抠
        #头为了返回，尾为了拼接
        dummy=ListNode()
        cur=dummy

        while list1!=None and list2!=None: #必须有值才能比较
            if list1.val<=list2.val: #拼接list1
                cur.next=list1
                list1=list1.next
                cur=cur.next
            else: #拼接list2
                cur.next=list2
                list2=list2.next
                cur=cur.next

        #把最后一个悬空的节点接上（一定是一个悬空一个有值），就算1悬空，2后面还有几个节点，也是排好序的
        if list1==None:
            cur.next=list2
        else:
            cur.next=list1

        return dummy.next