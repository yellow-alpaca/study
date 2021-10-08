# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ソートされたリンクリストの重複を削除する。
        重複削除用のheadを用意する。
        from LEETCODE (83. Remove Duplicates from Sorted List)
        https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        """ 
        # Time: O(n)
        # Space: O(1)
        copy = head
        while copy and copy.next:
            if copy.val == copy.next.val:
                copy.next = copy.next.next
            else:
                copy = copy.next
        return head
