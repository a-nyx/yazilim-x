class Solution2:
    def partition(self, linkedList, value):
        beforeStart = beforeEnd = afterStart = afterEnd = None
        node = linkedList.head
        while node:
            next = node.next
            node.next = None
            if node.data < value:
                if not beforeStart:
                    beforeStart = node
                    beforeEnd = node
                else:
                    beforeEnd.next = node
                    beforeEnd = node
            else:
                if not afterStart:
                    afterStart = node
                    afterEnd = node
                else:
                    afterEnd.next = node
                    afterEnd = node
            node = next

        if not beforeStart:
            linkedList.head = afterStart
        else:
            beforeEnd.next = afterStart
            linkedList.head = beforeStart
