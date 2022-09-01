class Stack:
    def __init__(self):
        self.base = None
        
    def push(self, item):
        if not self.base:
            self.base = Node(item)
        else:
            current = self.base
            while current.above: #while current.above != None
                current = current.above
            current.above = Node(item)
    
    def pop(self):
        #remember that the pop removes and returns the topmost value
        #from our stack
        if not self.base: # same thing as if self.base == None
            raise EmptyStackException("The stack is empty")
        if not self.base.above:
            datum = self.base.data
            self.base = None
            return datum
        current = self.base
        prev = None
        while current.above:
            prev = current
            current = current.above
        datum = current.data
        prev.above = None
        return datum
    
    
    def is_empty(self):
        if not self.base:
            return True
        return False
    
    def size(self):
        pass
    
    def peek(self):
        pass
