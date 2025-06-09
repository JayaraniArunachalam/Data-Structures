class Stack:
    def __init__(self):
        self.stack= []
    def push(self,*args):
        self.stack.extend(args)
        print("The items in the stack:\n",self.stack)
    def pop(self):
        if  len(self.stack)!=0:
            removed = self.stack.pop()
            print("The item",removed,"is removed")
        else:
            print("Stack is empty, pop operation cant be performed")
    def peek(self):
        if len(self.stack)!=0:
            print("The last item in the stack is ",self.stack[-1])
        else:
            print("The stack is empty")
    def is_empty(self):
        if len(self.stack)==0:
            print("Yes,The stack is empty")
        else:
            print("The stack is not empty")

s1 = Stack()
s1.push("Apples","Bananas","Grapes","Oranges",
             "Kiwi","Pomegranate")
s1.pop()
s1.peek()
s1.is_empty()

