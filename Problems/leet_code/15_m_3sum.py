# https://leetcode.com/problems/3sum/description/

## Topics
# => Array
# => Two Pointers
# => Sorting

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# Answers

# if builtin sort not allowed 
# def sort_list(self, ls: List[int]):
#     if ls[0] == ls[1] == ls[2]:
#         return
    
#     if ls[0] > ls[1]:
#         ls[0], ls[1] = ls[1], ls[0]

#     if ls[1] > ls[2]:
#         ls[1], ls[2] = ls[2], ls[1]
        
#     if ls[0] > ls[1]:
#         ls[0], ls[1] = ls[1], ls[0]
 
 

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        
        for i in range(len(nums) - 1):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums) - 1):
                    if i == j or j == k or i == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        scored_list = sorted([nums[i], nums[j], nums[k]])
                        if result_list.count(scored_list) == 0:
                            result_list.append(scored_list)
                        continue
        return result_list


input1 = [-1, 0, 1, 2, -1, -4]
# output [[-1,-1,2],[-1,0,1]]

input2 = [0, 1, 1]
# Output: []

input3 = [0, 0, 0]
# Output: [[0,0,0]]

sol = Solution()
print(sol.threeSum(input1))
print(sol.threeSum(input2))
print(sol.threeSum(input3))
