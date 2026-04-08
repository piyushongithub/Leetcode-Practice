class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None 
        self.next = None 

class Deque:
    
    def __init__(self):
        self.head = Node(-1) # dummy
        self.tail = Node(-1) # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        last_node = self.tail.prev 
        new_node = Node(value)
        new_node.next = self.tail 
        new_node.prev = last_node
        last_node.next = new_node
        self.tail.prev = new_node
        self.size+=1


    def appendleft(self, value: int) -> None:
        first_node = self.head.next 
        new_node = Node(value)
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node
        self.head.next = new_node
        self.size+=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev 
        prev_node = last_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        self.size-=1 
        return last_node.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        next_node = first_node.next
        self.head.next = next_node
        next_node.prev = self.head
        self.size-=1 
        return first_node.val
        
