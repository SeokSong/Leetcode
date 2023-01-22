class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if(index < 0 or self.size <= index):
            return -1

        currNode = self.head

        for _ in range(index):
            currNode = currNode.next

        return currNode.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if(self.size < index):
            return
        
        currNode = self.head
        newNode = ListNode(val)

        if(index <= 0):
            newNode.next = currNode
            self.head = newNode
        else:
            for _ in range(index -1):
                currNode = currNode.next
            newNode.next = currNode.next
            currNode.next = newNode
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if(index < 0 or self.size <= index):
            return
        
        currNode = self.head

        if index == 0:
            self.head = currNode.next
        else:
            for _ in range(index -1):
                currNode = currNode.next
            currNode.next = currNode.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)