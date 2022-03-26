class Solution2:
    def delete_dups(self, linkedList):
        prev = linkedList.head
        current = prev.next

        seen = set()
        seen.add(prev.data)

        while current:
            if current.data in seen:
                prev.next = current.next
                current = current.next
            else:
                seen.add(current.data)
                prev = prev.next
                current = current.next
