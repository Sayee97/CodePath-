# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def oddEvenList(self, head):
        odds = ListNode(0)
        evens = ListNode(0)
        oh =odds
        eh = evens
        odd = True
        while head:
            if odd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            odd = not odd
            head = head.next
        evens.next =None
        odds.next = eh.next
        
        return oh.next
            
                
                
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

