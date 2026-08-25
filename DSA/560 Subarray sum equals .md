<img width="1919" height="718" alt="image" src="https://github.com/user-attachments/assets/0b2900ed-c88d-497c-970c-4626b7f00fec" />

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        count = 0
        hashmap = {0: 1}

        for i in nums:
            prefixsum += i

            needed = prefixsum - k

            if needed in hashmap:
                count += hashmap[needed]

            if prefixsum in hashmap:
                hashmap[prefixsum] += 1
            else:
                hashmap[prefixsum] = 1

        return count
  ```

## PROBLEM

so in the ques we have given an array nums and an integer k and we have to return the total number of subarrays whose sum is equal to k.

like here nums = [1,2,3] and k = 3.

the subarrays whose sum is 3 are [1,2] and [3], so the answer will be 2.

## APPROACH

so here we use prefixsum and hashmap.

first we calculate the prefixsum while looping through the array.

then we use this formula:

needed = prefixsum - k

because if the current prefixsum is prefixsum and we want a subarray with sum k, then we need a previous prefixsum equal to prefixsum - k.

like nums = [1,2,3] and k = 3.

when we reach 2:

prefixsum = 1 + 2 = 3

so:

needed = 3 - 3 = 0

and 0 is already present in the hashmap, which means the subarray from the beginning [1,2] has sum 3.

then we store the prefixsum in the hashmap and its frequency as the value.

we store frequency instead of just the index because the same prefixsum can appear multiple times, and every previous occurrence can create a different subarray whose sum is k.

also we start with hashmap = {0: 1} because prefixsum 0 exists once before the array starts. this helps us count subarrays that start from index 0.

finally count contains the total number of subarrays whose sum is equal to k.

## CODE EXPLAINATION

```python
nums = [1,2,3]

k = 3

prefixsum = 0    -> prefixsum is used to calculate the running prefix sum.
count = 0        -> count stores the total number of subarrays whose sum is equal to k.
hashmap = {0: 1} -> hashmap stores prefixsum as the key and its frequency as the value.


{0: 1} means prefixsum 0 has appeared once before the array started.

for i in nums:
    prefixsum += i

-> looping through every element of nums and adding it to prefixsum.

for nums = [1,2,3] the prefixsum will be:

1 -> 3 -> 6

needed = prefixsum - k

-> calculating which previous prefixsum we need to get a subarray whose sum is k.

the formula is:

previous prefixsum = current prefixsum - k

for example when prefixsum = 3 and k = 3:

needed = 3 - 3 = 0

so we check if prefixsum 0 was seen before.

if needed in hashmap:
    count += hashmap[needed]

-> if needed is present in the hashmap, it means there are previous prefix sums that can create a subarray with sum k.

then we add its frequency to count.

we add the frequency instead of just 1 because the same prefixsum might have appeared multiple times.

if prefixsum in hashmap:
    hashmap[prefixsum] += 1
else:
    hashmap[prefixsum] = 1

-> after checking the needed prefixsum, we store the current prefixsum in the hashmap.

if the prefixsum already exists, increase its frequency by 1.

otherwise create a new key with frequency 1.

return count

-> returns the total number of subarrays whose sum is equal to k.
```
