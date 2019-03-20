class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


def removeNthNode(head,n):
    dummy=ListNode(0)
    dummy.next=head
    first=head
    length=0
    while first!=None:
        length=length+1
        first=first.next

    length=length-n
    first=dummy
    while length>0:
        length=length-1
        first=first.next
    first.next=first.next.next
    return dummy.next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)

a.next=b
b.next=c
c.next=d
d.next=e

print(a.val)
print(a.next.val)
print(a.next.next.val)
print(a.next.next.next.val)

f=removeNthNode(a,2)
print(f.val)
print(f.next.val)
print(f.next.next.val)
print(f.next.next.next.val)


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    first = head
    while first != None:
        length = length + 1
        first = first.next

    length = length - n
    first = dummy
    while length > 0:
        length = length - 1
        first = first.next
    first.next = first.next.next
    return dummy.next


a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)

a.next=b
b.next=c
c.next=d
d.next=e

f=removeNthFromEnd(a,2)
print(f.val)
print(f.next.val)
print(f.next.next.val)
print(f.next.next.next.val)