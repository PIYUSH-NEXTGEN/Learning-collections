<img width="1917" height="777" alt="image" src="https://github.com/user-attachments/assets/0e8fbe64-b75f-4514-bf3d-50aaa8f097aa" />


# SORT AN ARRAY

## PROBLEM -

the question is simple, we are given an unsorted array and we have to sort it without using built-in sorting functions.

for example:

```text
[4, 3, 1, 2]
```

we have to sort it and return:

```text
[1, 2, 3, 4]
```

---

# APPROACH -

we are using **merge sort** here.

we can sort an array in different ways also, but some sorting algorithms can take `O(n²)` time in the worst case.

here we need a better time complexity, so we use **merge sort**, which takes `O(n log n)` time.

the main idea of merge sort is:

```text
divide the array
        ↓
divide again
        ↓
keep dividing
        ↓
until every part has only 1 element
        ↓
merge the parts back in sorted order
```

for example:

```text
[4, 3, 1, 2]

       ↓ divide

[4, 3]     [1, 2]

    ↓          ↓

[4] [3]      [1] [2]
```

now every part has only one element.

then we start merging them in sorted order.

```text
[4] + [3] → [3, 4]

[1] + [2] → [1, 2]

[3, 4] + [1, 2] → [1, 2, 3, 4]
```

---

# CODE EXPLANATION -

first we create an empty array:

```python id="2p1x9r"
sorted_arr = []
```

this array will store the elements in sorted order while we merge the left and right arrays.

then:

```python id="f7k2qm"
i = 0
j = 0
```

we use two pointers.

`i` is used to keep track of the current element in the `left` array.

`j` is used to keep track of the current element in the `right` array.

both start from `0` because we start comparing from the first element.

---

### BASE CASE -

```python id="v2c8na"
if len(nums) <= 1:
    return nums
```

this is the base case of our recursion.

if the array has `0` or `1` element, it is already sorted.

for example:

```text
[5] → already sorted
[]  → already sorted
```

so we simply return it.

this is also what stops the recursion.

---

### FINDING MID -

```python id="4n1h8z"
mid = len(nums) // 2
```

here we find the middle index of the array.

for example:

```text
nums = [4, 3, 1, 2]

len(nums) = 4

4 // 2 = 2
```

so:

```text
mid = 2
```

---

### DIVIDING THE ARRAY -

```python id="j3s8bc"
left = self.sortArray(nums[:mid])
right = self.sortArray(nums[mid:])
```

here we divide the array into two parts.

```python id="j4w9qk"
nums[:mid]
```

gives the left part.

and:

```python id="a8c6fp"
nums[mid:]
```

gives the right part.

for:

```text
[4, 3, 1, 2]
```

we get:

```text
left  = [4, 3]
right = [1, 2]
```

but notice that we are calling `sortArray()` again on both parts.

so the array keeps getting divided until we reach arrays containing only one element.

---

### WHILE LOOP -

after the recursive calls return, both `left` and `right` are already sorted.

then we merge them:

```python id="w3q7kd"
while i < len(left) and j < len(right):
```

this means:

**keep comparing while both arrays still have elements left.**

we compare the current elements:

```python id="k8s1fz"
if left[i] <= right[j]:
```

if the current element of `left` is smaller or equal:

```python id="n4c2ma"
sorted_arr.append(left[i])
i += 1
```

we add `left[i]` to `sorted_arr`.

then we increment `i` so that we move to the next element of `left`.

otherwise:

```python id="x7d4pq"
else:
    sorted_arr.append(right[j])
    j += 1
```

we add `right[j]` because it is smaller.

then we increment `j` to move to the next element of `right`.

---

### EXAMPLE -

suppose:

```text
left  = [1, 4]
right = [2, 3]
```

initially:

```text
i = 0
j = 0
```

so we compare:

```text
left[i]  = 1
right[j] = 2
```

`1` is smaller, so:

```text
sorted_arr = [1]
i = 1
```

now compare:

```text
left[i]  = 4
right[j] = 2
```

`2` is smaller, so:

```text
sorted_arr = [1, 2]
j = 1
```

now compare:

```text
left[i]  = 4
right[j] = 3
```

`3` is smaller, so:

```text
sorted_arr = [1, 2, 3]
j = 2
```

now `j == len(right)`, so the while loop stops.

but `4` is still left in the `left` array.

---

### EXTEND -

this is where these two lines are important:

```python id="k6h2m1"
sorted_arr.extend(left[i:])
sorted_arr.extend(right[j:])
```

the while loop stops when **one of the arrays becomes completely processed**.

there can still be some elements left in the other array.

in our example:

```text
left  = [1, 4]
right = [2, 3]

sorted_arr = [1, 2, 3]

4 is still left in left
```

so:

```python id="a9m5q2"
left[i:]
```

gives:

```text
[4]
```

and:

```python id="s7d3kx"
sorted_arr.extend(left[i:])
```

adds it to `sorted_arr`.

now:

```text
[1, 2, 3, 4]
```

we do the same for `right[j:]`.

if nothing is left, it simply adds nothing.

---

### RETURN -

finally:

```python id="m2v8za"
return sorted_arr
```

we return the sorted array.

---

# IMPORTANT POINT -

the most important thing to understand in merge sort is that **we don't sort the whole array at once**.

we:

```text
divide
  ↓
divide
  ↓
divide
  ↓
single elements
  ↓
compare
  ↓
merge
  ↓
sorted array
```

also, the `while` loop only compares elements while **both left and right arrays have elements**.

that's why we need:

```python id="r5n8cx"
sorted_arr.extend(left[i:])
sorted_arr.extend(right[j:])
```

to add whatever elements are still remaining.

---

# TIME COMPLEXITY -

```text
O(n log n)
```

we divide the array into halves, which gives us `log n` levels.

at every level, we process all `n` elements while merging.

so:

```text
n × log n = O(n log n)
```

# SPACE COMPLEXITY -

```text
O(n)
```

because we create new arrays during the merge process and recursion.






