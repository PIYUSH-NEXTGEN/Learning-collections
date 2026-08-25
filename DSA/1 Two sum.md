<img width="1915" height="730" alt="image" src="https://github.com/user-attachments/assets/ebeaa5b8-2798-401d-a73a-714df0f0072b" />

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
```

# PROBLEM

so in the ques we have given an array nums and an integer target and we have to find two different elements whose sum is equal to target.

we have to return the indices of those two elements.

like here nums = [2,7,11,15] and target = 9.

here 2 + 7 = 9, so the indices are 0 and 1, therefore the answer will be [0,1].

# APPROACH

so here we use two loops to check every possible pair of elements in the array.

first loop takes one element using index i.

then second loop takes another element using index j.

we check two conditions:

i != j

this makes sure that we are not using the same element twice.

and:

nums[i] + nums[j] == target

this checks if the sum of the two elements is equal to the target.

if both conditions are true, we return their indices [i,j].

for example nums = [2,7,11,15] and target = 9:

2 + 2 -> not allowed because i == j

2 + 7 = 9 -> target found

so we return [0,1].

# CODE EXPLAINATION

```python
nums = [2,7,11,15]

target = 9

for i in range(len(nums)): -> first loop through the indices of nums.

for nums = [2,7,11,15], i will be 0, 1, 2, and 3.

for j in range(len(nums)): -> second loop also goes through all the indices of nums,this allows us to check every possible pair of elements.

if i != j and nums[i] + nums[j] == target: -> checking two conditions.

i != j means the two indices must be different, so we don't use the same element twice.

nums[i] + nums[j] == target checks if the sum of the two elements is equal to target.

return [i, j] -> if we find two elements whose sum is equal to the target, we return their indices.

for example:

nums[0] + nums[1]

2 + 7 = 9

so it returns [0,1].
```
