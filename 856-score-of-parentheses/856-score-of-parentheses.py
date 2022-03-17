class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        score = 0
        for ch in S:
            if ch == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score , 1)
        return score