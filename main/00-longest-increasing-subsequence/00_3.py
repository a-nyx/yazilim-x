class Solution:
    def __init__(self):
        self.helper_array = []

    def update_helper_array(self, number):
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
        for num in arr:
            self.update_helper_array(num)
        return len(self.helper_array)


# TESTING

test_cases = [
    # [array, expected_result]
    [[1, 2, 3, 4, 5], 5],
    [[10, 22, 9, 33, 21, 50, 41, 60, 80], 6],
    [[10, 9, 2, 5, 3, 7, 101, 18], 4],
    [[7, 7, 7, 7, 7, 7, 7], 1],
    [[99, 44, 55, 2, 66, 3, 4, 5], 4],
    [[1, 3, 6, 7, 9, 4, 10, 5, 6], 6]
]

failed = False
for [arr, expected_result] in test_cases:
    if Solution().longest_increasing_subsequence(arr) != expected_result:
        failed = True
        print("FAILED: arr:", arr, "expected_result:", expected_result)

if not failed:
    print("All test cases passed.")
