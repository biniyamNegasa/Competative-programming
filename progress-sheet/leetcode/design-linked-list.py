class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index>=self.len:
            return -1
        temp = self.head
        while index:
            temp = temp.nxt
            index-=1
        return temp.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.nxt = self.head
        self.head = node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            temp = self.head
            while temp.nxt:
                temp = temp.nxt
            temp.nxt = Node(val)
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.len:
            return
        if not index:
            self.addAtHead(val)
        else:
            temp = self.head
            while index>1:
                temp = temp.nxt
                index-=1
            node = Node(val, temp.nxt)
            temp.nxt = node
            self.len+=1
                
    def deleteAtIndex(self, index: int) -> None:
        if index>= self.len:
            return
        if not index:
            self.head = self.head.nxt
        else:
            temp = self.head
            while index>1:
                temp = temp.nxt
                index-=1
            t2 = temp.nxt
            temp.nxt = t2.nxt
            t2.nxt = None
        self.len-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)