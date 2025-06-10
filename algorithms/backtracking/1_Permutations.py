from typing import List


def find_all_permutations(nums: List[int]) -> List[List[int]]:
    result_list = []
    current_permutation = []
    used = [False] * len(nums)  # Initialize a boolean array to track used numbers

    def backtrack(current_permutation_arg, nums_arg, used_arg, result_list_arg):
        # Base Case: If the current permutation is complete
        if len(current_permutation_arg) == len(nums_arg):
            result_list_arg.append(list(current_permutation_arg))  # Add a copy!
            return

        # Iterate through all possible choices
        for i in range(len(nums_arg)):
            # If the number at index i hasn't been used yet
            if not used_arg[i]:
                # 1. Make a choice
                current_permutation_arg.append(nums_arg[i])
                used_arg[i] = True

                # 2. Recurse (explore further)
                backtrack(current_permutation_arg, nums_arg, used_arg, result_list_arg)

                # 3. Unmake the choice (Backtrack)
                used_arg[i] = False
                current_permutation_arg.pop()

    # Initial call to start the backtracking process
    backtrack(current_permutation, nums, used, result_list)
    return result_list


ls1 = [1, 2, 4]
print(find_all_permutations(ls1))
