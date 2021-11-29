class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        left_part = ['(', '{', '[']
        right_part = [')', '}', ']']
        stack = []
        for c in list(s):
            if c in left_part:
                stack.append(c)
            elif c in right_part:
                if stack == []:
                    stack.append(c)
                elif stack[-1] in left_part and \
                    right_part.index(c) == left_part.index(stack[-1]):
                    stack.pop(-1)
                else:
                    stack.append(c)
        return (stack == [])

from collections import deque
class Solution:
    """减小了解空间"""
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = deque()
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] in left and \
                right.index(char) == left.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        left = ["(", "{", "["]
        right = [")", "}", "]"]

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char in left:
                    stack.append(char)
                else:
                    if stack[-1] in left and left.index(stack[-1]) == right.index(char):
                        stack.pop()
                    else:
                        stack.append(char)
        return len(stack) == 0
