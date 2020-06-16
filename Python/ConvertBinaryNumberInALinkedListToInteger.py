class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        n = []
        
        while head != None:
            n.append(head.val)
            head = head.next
        
        return int("".join(map(str,n)),2)
