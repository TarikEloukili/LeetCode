# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0  
 
        if l1.val + l2.val < 10:
            result = ListNode(l1.val + l2.val)
            carry = 0
        else:
            result = ListNode((l1.val + l2.val) - 10)
            carry = 1
        
        current1 = l1.next
        current2 = l2.next
        current_result = result
        
      
        while current1 and current2:
            total = current1.val + current2.val + carry
            if total < 10:
                current_result.next = ListNode(total)
                carry = 0
            else:
                current_result.next = ListNode(total - 10)
                carry = 1
            
            current1 = current1.next
            current2 = current2.next
            current_result = current_result.next
        
  
        while current1:
            total = current1.val + carry
            if total < 10:
                current_result.next = ListNode(total)
                carry = 0
            else:
                current_result.next = ListNode(total - 10)
                carry = 1
            
            current1 = current1.next
            current_result = current_result.next
        
 
        while current2:
            total = current2.val + carry
            if total < 10:
                current_result.next = ListNode(total)
                carry = 0
            else:
                current_result.next = ListNode(total - 10)
                carry = 1
            
            current2 = current2.next
            current_result = current_result.next
        
  
        if carry > 0:
            current_result.next = ListNode(carry)
        
        return result
