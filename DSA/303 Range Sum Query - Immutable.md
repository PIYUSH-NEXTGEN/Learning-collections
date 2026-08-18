<img width="1899" height="782" alt="image" src="https://github.com/user-attachments/assets/c3ed9d4f-eb47-45b4-92c9-799152c71bbc" />

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in nums:
            total += i
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]
```

So in this problem, we first make a **prefix array** from the given array. A prefix array stores the sum of all elements from the beginning up to the current index. For example, `[1, 2, 3]` becomes `[1, 3, 6]` because `1`, `1+2 = 3`, and `1+2+3 = 6`.

**Why prefix sum?** Because we have to perform multiple range-sum queries. Instead of calculating the sum again and again for every query, we calculate the cumulative sums once and then use them to get each range sum in `O(1)` time.

```python
self.prefix = []
```

→ Creates an empty array to store the prefix sums.

```python
total = 0
```

→ Stores the **running sum**. We start with `0` because we haven't added anything yet.

```python
for i in nums:
```

→ Loops through every element in `nums`.

```python
total += i
```

→ Adds the current element to the previous running sum. For `[-2, 0, 3, -5, 2, -1]`, the totals become `-2, -2, 1, -4, -2, -3`.

```python
self.prefix.append(total)
```

→ Stores each running total in the prefix array, so we finally get `[-2, -2, 1, -4, -2, -3]`.

```python
if left == 0:
```

→ Checks if the requested range starts from index `0`. For example, `sumRange(0, 2)`.

```python
return self.prefix[right]
```

→ If `left` is `0`, we don't need to subtract anything. `prefix[2] = 1`, which is `-2 + 0 + 3 = 1`.

```python
else:
```

→ If the range does not start from `0`, we need to remove the elements before `left`.

```python
return self.prefix[right] - self.prefix[left - 1]
```

→ `prefix[right]` gives the sum from the beginning up to `right`, while `prefix[left - 1]` gives the unwanted part before `left`. For `sumRange(2, 5)`: `prefix[5] - prefix[1] = -3 - (-2) = -1`.
### How does `self.prefix[right] - self.prefix[left - 1]` work?

Suppose:

```python
nums = [-2, 0, 3, -5, 2, -1]
```

and the query is:

```python
sumRange(2, 5)
```

So:

```text
left = 2
right = 5
```

We want:

```text
3 + (-5) + 2 + (-1) = -1
```

Our prefix array is:

```text
prefix = [-2, -2, 1, -4, -2, -3]
index     0   1  2   3   4   5
```

```python
self.prefix[right]
```

→ Since `right = 5`, `self.prefix[5] = -3`. This gives the sum of everything from index `0` to `5`:

```text
-2 + 0 + 3 - 5 + 2 - 1 = -3
```

But we only want the elements from index `2` to `5`, so we need to remove the elements before index `2`:

```text
-2 + 0 = -2
```

```python
self.prefix[left - 1]
```

→ Since `left = 2`, `left - 1 = 1`, so `self.prefix[1] = -2`. This gives the sum of everything before index `2`.

Now subtract:

```text
self.prefix[5] - self.prefix[1]

= -3 - (-2)

= -1
```

And `-1` is exactly:

```text
3 + (-5) + 2 + (-1) = -1
```

### In simple words

```text
prefix[right]     → everything up to right
prefix[left - 1]  → unwanted part before left

everything - unwanted part = required range sum
```

That's why we use:

```python
return self.prefix[right] - self.prefix[left - 1]
```
