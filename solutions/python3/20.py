class Solution:
    def isValid(self, s):
        brackets_stack, lefts, rights = [], ("(", "[", "{"), (")", "]", "}") 
        for char in s:
            if char in lefts: 
                brackets_stack.append(char)
            elif not brackets_stack or lefts.index(brackets_stack.pop()) != rights.index(char): 
                return False
        return not brackets_stack


    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif not stack:
                return False
            elif char == ')' and stack.pop() != '(':
                return False
            elif char == ']' and stack.pop() != '[':
                return False
            elif char == '}' and stack.pop() != '{':
                return False
        return not stack


if __name__ == '__main__':
    zhushi = Solution()
    s = "()[]{}"
    print(zhushi.is_valid(s))


