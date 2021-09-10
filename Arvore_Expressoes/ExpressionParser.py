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

def split(word):
    return [char for char in word]

def infixToPostList(exp):
    stack = Stack()
    stack.push('#')

    output = []

    splitExp = split(exp)
    op = 0
    
    while op < len(exp):
        if(splitExp[op] == ' '):
            op += 1
        elif(splitExp[op].isnumeric() or splitExp[op].isalpha()):
            strp = ''
            while(splitExp[op].isnumeric() or splitExp[op].isalpha()):
                strp += splitExp[op]
                op+=1
                if(op == len(exp)):
                    break
            output.append(strp)
            
        elif (splitExp[op] == '('):
            stack.push(splitExp[op])
            op += 1
        elif (splitExp[op] == ')'):
            while (not stack.isEmpty() and stack.peek() != '('):
                item = stack.pop()
                output.append(item)
            stack.pop()
            op += 1
        else:
            while (not stack.isEmpty() and precedence(splitExp[op]) <= precedence(stack.peek())):
                output.append(stack.pop())
            stack.push(splitExp[op])
            op += 1
    while (stack.peek() != '#'):
           output.append(stack.peek())
           stack.pop()

    return output

def infixToPost(exp):
    stack = Stack()
    stack.push('#')

    output = []

    splitExp = split(exp)
    op = 0
    
    while op < len(exp):
        if(splitExp[op] == ' '):
            op += 1
        elif(splitExp[op].isnumeric() or splitExp[op].isalpha()):
            strp = ''
            while(splitExp[op].isnumeric() or splitExp[op].isalpha()):
                strp += splitExp[op]
                op+=1
                if(op == len(exp)):
                    break
            output.append(strp)
            
        elif (splitExp[op] == '('):
            stack.push(splitExp[op])
            op += 1
        elif (splitExp[op] == ')'):
            while (not stack.isEmpty() and stack.peek() != '('):
                item = stack.pop()
                output.append(item)
            stack.pop()
            op += 1
        else:
            while (not stack.isEmpty() and precedence(splitExp[op]) <= precedence(stack.peek())):
                output.append(stack.pop())
            stack.push(splitExp[op])
            op += 1
    while (stack.peek() != '#'):
           output.append(stack.peek())
           stack.pop()
    outputJoin = ''.join(output)

    return outputJoin
