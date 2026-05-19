class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for c in s:
            if c in "({[":
                valid_stack.append(c)
            else:
                if valid_stack and valid_stack[-1] == mapping[c]:
                    valid_stack.pop()
                else:
                    return False
        if len(valid_stack) == 0:
            return True
        return False