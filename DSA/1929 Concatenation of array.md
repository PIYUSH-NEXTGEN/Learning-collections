<img width="1919" height="719" alt="image" src="https://github.com/user-attachments/assets/fbca5d4d-bbc9-428f-9a75-3d68d2b2e3d7" />

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(i)

        ans += nums

        return ans
  ```


# PROBLEM

so in the ques we have given an array `nums` and we have to return the array with itself concatenated. like here `nums = [1,2,3]` so we have to return `[1,2,3,1,2,3]`. basically we have to put the same array two times one after another.

# APPROACH

so here we first create a blank array `ans` where we will store the elements.

then we loop through `nums` and append every element into `ans`. after that `ans` already contains the original array.

then we use `ans += nums` which adds the complete `nums` array again at the end of `ans`.

so if `nums = [1,2,3]`:

`ans = [1,2,3]`

then `ans += nums`

`ans = [1,2,3,1,2,3]`

and finally we return `ans`.

# CODE EXPLAINATION

```python
nums = [1,2,3]

ans = []

creating a blank array to store the elements of nums.

for i in nums:
    ans.append(i)

-> looping through nums and adding every element into ans. So after this loop ans becomes [1,2,3].

ans += nums

-> adding the complete nums array again at the end of ans. So ans becomes [1,2,3,1,2,3].

return ans

-> returns the concatenated array [1,2,3,1,2,3].
```
