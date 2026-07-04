# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return list1
        if not list1: return list2
        if not list2: return list1

        res_list = ListNode(0, None)
        dummy = res_list
        while list1 or list2:
            val1 = list1.val if list1 else 101
            val2 = list2.val if list2 else 101
            if val1 > val2: 
                res_list.next = ListNode(val2, None)
                list2 = list2.next if list2 else None
            else: 
                res_list.next = ListNode(val1, None)
                list1 = list1.next if list1 else None

            res_list = res_list.next

        return dummy.next
            
