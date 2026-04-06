class Node:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def isEmpty(self) -> bool:
        if not self.head.next:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = Node(value,self.tail)
        self.tail.next = new_node
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        old = self.head.next
        new_node = Node(value,self.head,old)
        if old:
            old.prev = new_node
        else:
            self.tail = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.tail.prev:
            end = self.tail
            temp = self.tail.prev
            temp.next = None 
            self.tail = temp
            return end.val
        return -1
        
    def popleft(self) -> int:
        if self.head.next:
            start = self.head.next
            temp = start.next
            self.head.next = temp
            if temp:
                temp.prev = self.head 
            else:
                self.tail = self.head
            
            return start.val
        return -1
        
