# Solution 1: O(n^2) time, O(1) space????
class Solution1:
    def partition(self, linkedList, value):
        node = linkedList.head
        head = node
        prev = None
        while node:
            if node.data < value and prev:
                prev.next = node.next
                node.next = head
                head = node
                node = prev.next
            else:
                prev = node
                node = node.next

        linkedList.head = head
