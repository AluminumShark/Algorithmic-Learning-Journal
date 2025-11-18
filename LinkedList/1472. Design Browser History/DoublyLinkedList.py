class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val      # Current page URL
        self.prev = prev    # Link to the previous page
        self.next = next    # Link to the next page

class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize browser with homepage as the first node
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        # Visiting a new page clears all forward history
        self.curr.next = None
        newPage = ListNode(url)
        # Link the new page with the current page
        self.curr.next = newPage
        newPage.prev = self.curr
        # Move current pointer to the new page
        self.curr = newPage

    def back(self, steps: int) -> str:
        # Move back up to 'steps' times or until no previous page
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # Move forward up to 'steps' times or until no next page
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
