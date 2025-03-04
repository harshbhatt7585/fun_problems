"""
**Remove N-th Node from End of Linked List**

Given a linked list, remove the n-th node from the end and return the modified list.

**Example:**

Input: 1 -> 2 -> 3 -> 4 -> 5,  n = 2

Output: 1 -> 2 -> 3 -> 5
"""

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' --> '.join(elements))


def remove_nth(head: LinkedList):
    curr = head
    prev = None
    if curr.next == None:
        head = None
    else:
        while curr:
            next_node = curr.next
            prev = curr
            curr = next_node
            if next_node.next == None:
                prev.next = None
                break

    return head


if __name__ == "__main__":
    n = 10
    node = LinkedList(val=0)
    for i in range(n-1):
        node = LinkedList(val=i+1, next=node)
    
    display(node)

    new_ll = remove_nth(node)
    display(new_ll)