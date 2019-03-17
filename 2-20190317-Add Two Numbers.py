class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


def addTwoNumbers(l1,l2):
    carry=0
    n=root=ListNode(0)
    while l1 or l2 or carry:
        v1=v2=0
        if l1:
            v1=l1.val
            l1=l1.next
        if l2:
            v2=l2.val
            l2=l2.next
        carry,val=divmod(v1+v2+carry,10)
        n.next=ListNode(val)
        n=n.next
    return root.next

l1=ListNode(1)
l3=ListNode(3)
l4=ListNode(4)

l2=ListNode(2)
l5=ListNode(5)

l1.next=l3
l3.next=l4
l2.next=l5

head=addTwoNumbers(l1,l2)
print(head.val)
print(head.next.val)
print(head.next.next.val)
