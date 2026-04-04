class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val
            curr = curr.next
            i+=1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # if list was empty before
        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i=0
        while curr.next:
            if index==i:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr
                return True
            curr = curr.next
            i+=1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr=curr.next
        return res
        
