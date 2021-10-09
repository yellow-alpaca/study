class Solution:
    def isValid(self, s: str) -> bool:
        """
        カッコの閉じ方が正しければTure。
        文字列をリストに入れ、閉じカッコはリストの最後尾との整合を検証する。
        from LEETCODE (20. Valid Parentheses)
        https://leetcode.com/problems/valid-parentheses/
        """
        mapping = {')': '(', '}': '{', ']':'['}
        stack = []
        try:
            for i in s:
                # 詳細は下部のコメント
                if i not in mapping:
                    stack.append(i)
                elif i in mapping and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
        except:
            return False

        return stack == []

# 愚直に書いた場合：
#  最初に閉じカッコがあるとエラーとなるためexceptで拾っている
#             for i in s:
#                 if i in ['(', '{', '[']:
#                     stack.append(i)
#                 elif i == ')' and stack[-1] == '(':
#                     stack.pop()
#                 elif i == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif i == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False
