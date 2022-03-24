# Solution 1: O(n^2) time, O(1) space
class Solution1:
    def delete_dups(self, linkedList):
        current = linkedList.head
        while current and current.next:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
