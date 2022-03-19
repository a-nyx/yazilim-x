class Solution:
    def __init__(self):
        # helper_array stores the smallest tail of all increasing subsequences with length i+1 in tails[i]
        # for more info: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
        self.helper_array = []

    def update_helper_array(self, number):
        """Inserts number into helper_array by binary search"""
        start = 0
        end = len(self.helper_array)

        while start != end:
            mid = (start + end) // 2
            if self.helper_array[mid] >= number:
                end = mid
            else:
                start = mid + 1

        if start < len(self.helper_array):
            self.helper_array[start] = number
        else:
            self.helper_array.append(number)

    def longest_increasing_subsequence(self, arr):
        """Returns the length of the longest increasing subsequence"""
        for num in arr:
            self.update_helper_array(num)
        return len(self.helper_array)


# TESTING

test_cases = [
    # [array, expected_result]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10],
    [[10, 22, 9, 33, 21, 50, 41, 60, 80], 6],
    [[10, 9, 2, 5, 3, 7, 101, 18], 4],
    [[7, 7, 7, 7, 7, 7, 7], 1],
    [[99, 44, 55, 2, 66, 3, 4, 5], 4],
    [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6],
    [[3, 2, 1, 0], 1],
    [[99], 1],
    [[50, 3, 10, 7, 40, 80], 4],
    [[11, 1, 12, 2, 13, 3, 14, 4, 15, 5, 16, 6], 6],
]

is_failed = False
for [arr, expected_result] in test_cases:
    actual_result = Solution().longest_increasing_subsequence(arr)
    if actual_result != expected_result:
        is_failed = True
        print("FAILED: arr:", arr, "expected_result:",
              expected_result, "actual_result:", actual_result)
        break

if not is_failed:
    print("All test cases passed.")
