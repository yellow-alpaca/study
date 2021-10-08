# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        リンクリストが循環構造になっているかを判定する。
        fastとslowでリンクを辿り、双方が一致するなら、
        循環して追いついたことが分かる。
        from LEETCODE (141. Linked List Cycle)
        https://leetcode.com/problems/linked-list-cycle/
        """
        # Time: O(n)
        # Space: O(1)
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next        
        return True
