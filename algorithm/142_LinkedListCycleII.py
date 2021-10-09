# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        リンクリストの循環位置を特定する。
        fastとslowで一致を確認した後、slowをheadに戻し、fastは1つずつ推移とする。
        slowとfastが重なった点が循環位置となる。
        from LEETCODE (142. Linked List Cycle II)
        https://leetcode.com/problems/linked-list-cycle-ii/
        """
        # Time: O(n)
        # Space: O(1)
        if head is None:
            return None
        
        # ループの判定
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        # 循環開始位置の特定
        slow = head
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
