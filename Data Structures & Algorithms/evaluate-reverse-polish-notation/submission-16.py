class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                if token == "+":
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(n1+n2)
                elif token == "-":
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(n1-n2)
                elif token == "*":
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(n1*n2)
                elif token == "/":
                    n1, n2 = stack.pop(), stack.pop()

                    stack.append(int(n2/n1))
        
        return stack.pop()