class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.now = self.head

    def visit(self, url: str) -> None:
        node = ListNode(url,None, self.now)
        self.now.next = node
        self.now = self.now.next

    def back(self, steps: int) -> str:
        x = 0
        while x<steps and self.now.prev:
            self.now = self.now.prev
            x+=1
        return self.now.val

    def forward(self, steps: int) -> str:
        x = 0
        while x<steps and self.now.next:
            self.now = self.now.next
            x+=1
        return self.now.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)