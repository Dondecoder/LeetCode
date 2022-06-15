class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def twomergedList(self, list1: ListNode, list2: ListNode):
        dummy = ListNode()
        fake_pointer = dummy

        while list1 and list2:
            if list1.val > list2.val:
                fake_pointer.next = list2
                list2 = list2.next
            else:
                fake_pointer.next = list1
                list1 = list1.next
            fake_pointer = fake_pointer.next
        if list1 is None:
            fake_pointer.next = list2
        else:
            fake_pointer.next = list1
        return dummy.next