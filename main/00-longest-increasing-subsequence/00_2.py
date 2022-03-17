class Solution:
    def longest_increasing_subsequence(self, arr):
        if not arr:
            return 0

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
