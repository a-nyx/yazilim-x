class Solution:
    def longest_increasing_subsequence(self, arr):
        """Returns the length of the longest increasing subsequence"""
        if not arr:
            return 0

        # helper_array[i] is the length of the longest increasing subsequence including arr[i]
        helper_array = [1]
        longest = 1
        for arr_i in range(1, len(arr)):
            maximum_so_far = 1
            for helper_i in range(0, arr_i):
                if arr[helper_i] < arr[arr_i] and helper_array[helper_i] + 1 > maximum_so_far:
                        maximum_so_far = helper_array[helper_i] + 1

            longest = maximum_so_far if maximum_so_far > longest else longest
            helper_array.append(maximum_so_far)

        return longest


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
    [[1, 3, 6, 7, 9, 4, 10, 5, 6], 6]
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
