class Stack:
    items = None
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def precedence(c):
    if(c == '+' or c == '-'):
        return 1
    elif (c == '*' or c == '/'):
        return 2
    elif (c == '^'):
        return 3
    else:
        return 0
        
def infixToPost(exp):
    stack = Stack()
    stack.push('#')
    output = []
    for c in exp.split():
        if (c.isnumeric() or c.isalpha()):
            output.append(c)
        elif (c == '('):
            stack.push(c)
        elif (c == '^'):
            stack.push(c)
        elif (c == ')'):
            while (not stack.isEmpty() and stack.peek() != '('):
                item = stack.pop()
                output.append(item)
            stack.pop()
        else:
            if(precedence(c) > precedence(stack.peek())):
                stack.push(c)
            else:
                while (not stack.isEmpty() and precedence(c) <= precedence(stack.peek())):
                    item = stack.pop()
                    output.append(item)

                output.append(c)
    while (stack.peek() != '#'):
        output.append(stack.peek())
        stack.pop()
    outputJoin = ''.join(output)
    return outputJoin
