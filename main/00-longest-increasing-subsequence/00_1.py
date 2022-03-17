class Solution:
    def __init__(self):
        self.longest = 0

    def LIS_helper(self, arr, index):
        maximum_so_far = 1

        for i in range(0, index):
            if arr[i] < arr[index]:
                maximum_until_i = self.LIS_helper(arr, i)
                if maximum_until_i + 1 > maximum_so_far:
                    maximum_so_far = maximum_until_i + 1

        if maximum_so_far > self.longest:
            self.longest = maximum_so_far

        return maximum_so_far

    def longest_increasing_subsequence(self, arr):
        self.LIS_helper(arr, len(arr)-1)
        return self.longest


# TESTING

test_cases = [
    # [array, expected_result]
    [[1, 2, 3, 4, 5], 5],
    [[10, 22, 9, 33, 21, 50, 41, 60, 80], 6],
    [[10, 9, 2, 5, 3, 7, 101, 18], 4],
    [[7, 7, 7, 7, 7, 7, 7], 1],
    [[99, 44, 55, 2, 66, 3, 4, 5], 4]
]

failed = False
for [arr, expected_result] in test_cases:
    if Solution().longest_increasing_subsequence(arr) != expected_result:
        failed = True
        print("FAILED: arr:", arr, "expected_result:", expected_result)

if not failed:
    print("All test cases passed.")
