<img width="1919" height="791" alt="image" src="https://github.com/user-attachments/assets/320a6ac1-2344-482d-82b7-17683619261c" />

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else :
                seen.add(i)
            
        return False
```

# PROBLEM

so in the ques we have given an array `nums` and we have to check if there is any duplicate element in the array or not.

if any element appears more than one time then we have to return `True`, otherwise we return `False`.

like here `nums = [1,2,3,1]`, `1` is present two times so it contains a duplicate and the answer will be `True`.

but if `nums = [1,2,3,4]`, every element is unique so the answer will be `False`.

# APPROACH

so here we use a **set** to keep track of the elements that we have already seen.

first we create an empty set called `seen`.

then we loop through every element of `nums`.

for every element we check if it is already present in `seen`.

if it is already present, it means that we have seen this element before, so it is a duplicate and we immediately return `True`.

otherwise we add that element into `seen` and continue the loop.

if the complete array is checked and we never find a duplicate, then we return `False`.

for example `nums = [1,2,3,1]`:

`1` -> not in set -> add `1`

`2` -> not in set -> add `2`

`3` -> not in set -> add `3`

`1` -> already in set -> duplicate found -> return `True`

# CODE EXPLAINATION

```python
nums = [1,2,3,1]
seen = set()  -> creating an empty set called seen where we will store the elements that we have already seen.

for i in nums:  -> looping through every element of nums one by one.

if i in seen:
    return True  -> checking if the current element i is already present in seen.

if it is already present, it means the same element appeared before, so it is a duplicate and we return True.

else:
    seen.add(i) -> if the current element is not already present in seen, we add it to the set so we can check it against the upcoming elements.

return False    -> if the loop finishes without finding any duplicate element, it means every element is unique, so we return False.
