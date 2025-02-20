class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                # stack[-1] = top of the stack
                while stack[-1] != "[":
                    # add to the beginning
                    substr = stack.pop() + substr
                # ensure opening bracket is popped
                stack.pop()
            
                # getting k digit
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)
