# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        
        
        def add(l1,l2,c):
            val = l1.val+l2.val+c
            rem = val%10
            c = val//10
            
            ans = ListNode(rem)
            
            if l1.next!=None or l2.next!=None or c!=0:
                if l1.next==None:
                    l1.next = ListNode(0)
                if l2.next==None:
                    l2.next = ListNode(0)
                ans.next = add(l1.next,l2.next,c)
                print(ans)
            return ans
        
        return add(l1,l2,0)
        