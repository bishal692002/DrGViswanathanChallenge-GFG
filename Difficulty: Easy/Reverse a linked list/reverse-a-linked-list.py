"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        current = head
        prev  = None
        while current != None:
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev
            