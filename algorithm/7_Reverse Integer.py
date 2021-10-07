class Solution:
    def reverse(self, x: int) -> int:
        """
        10進数を逆順に表示する。範囲外は0とする。
        符号を取得した後、intをstrとして扱う。
        https://leetcode.com/problems/reverse-integer/
        """
        # Time: O(log(n))
        # Space: O(1)
        sign = [1, -1][x <  0]
        revert = sign * int(str(abs(x))[::-1])
        return revert if -(2**31)-1 < revert < 2**31 else 0        
 
