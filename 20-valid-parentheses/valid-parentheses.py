class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for parenthese in s:
            if parenthese in mapping:
                top = stack.pop() if stack else "#"
                if top != mapping[parenthese]:
                    return False
            else:
                stack.append(parenthese)
        return len(stack) == 0

