<img width="1919" height="730" alt="image" src="https://github.com/user-attachments/assets/7032a646-4888-4fb9-a680-e2a68c4de0ea" />

# SORT COLORS - #75

## PROBLEM -

the problem is simple. we are given an array containing only `0`, `1`, and `2`.

we have to sort the array in-place so that:

```text
0s -> 1s -> 2s
```

for example:

```text
nums = [2,0,2,1,1,0]

output = [0,0,1,1,2,2]
```

we should not use a built-in sorting function.

---

# APPROACH -

we are using the **Dutch National Flag algorithm** here.

instead of sorting the array normally, we divide the array into 3 parts:

```text
0s | 1s | unknown | 2s
```

for this we use 3 pointers:

```text
low
mid
high
```

their job is:

* `low` -> where the next `0` should go
* `mid` -> current element we are checking
* `high` -> where the next `2` should go

initially:

```python
low = 0
mid = 0
high = len(nums) - 1
```

---

# CODE EXPLANATION -

## INITIALIZATION -

```python
low = 0
mid = 0
high = len(nums) - 1
```

we start `low` and `mid` from the beginning of the array.

`high` starts from the last index.

for example:

```text
nums = [2,0,2,1,1,0]

index   0  1  2  3  4  5
        ------------------
nums    2  0  2  1  1  0

low = 0
mid = 0
high = 5
```

---

## WHILE LOOP -

```python
while mid <= high:
```

we keep checking elements until `mid` crosses `high`.

`mid` is the pointer that checks the current element.

---

# CASE 1 - NUMS[MID] == 0

```python
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]

    low += 1
    mid += 1
```

if the current element is `0`, we want to move it to the left side.

so we swap:

```python
nums[low], nums[mid] = nums[mid], nums[low]
```

then both `low` and `mid` are increased.

why?

because after putting `0` at `low`, that position is correct.

and the element that came to `mid` also needs to be checked, but in this case because `low <= mid`, the position is safe to move forward.

---

# CASE 2 - NUMS[MID] == 1

```python
elif nums[mid] == 1:
    mid += 1
```

if the current element is `1`, we don't need to move it.

`1` belongs in the middle.

so we simply move `mid` forward:

```text
mid -> next element
```

---

# CASE 3 - NUMS[MID] == 2

```python
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

if the current element is `2`, we want to move it to the right side.

so we swap the current element with the element at `high`:

```python
nums[mid], nums[high] = nums[high], nums[mid]
```

then:

```python
high -= 1
```

because the `2` that we moved to `high` is now in its correct position.

### IMPORTANT -

notice that we **do not increase `mid` here**.

why?

because the element that came from `high` into `mid` has not been checked yet.

it could be:

```text
0
1
2
```

so we need to check `nums[mid]` again.

this is one of the most important parts of this algorithm.

---

# EXAMPLE -

let:

```text
nums = [2,0,2,1,1,0]
```

initially:

```text
low = 0
mid = 0
high = 5
```

`nums[mid] = 2`

so swap `mid` and `high`:

```text
[0,0,2,1,1,2]
```

now:

```text
high = 4
mid = 0
```

we don't increase `mid` because the new element at `mid` still needs to be checked.

---

now:

```text
nums[mid] = 0
```

swap `low` and `mid`:

```text
[0,0,2,1,1,2]
```

then:

```text
low = 1
mid = 1
```

---

now:

```text
nums[mid] = 0
```

move it to the `low` position.

```text
low = 2
mid = 2
```

---

now:

```text
nums[mid] = 2
```

swap with `high`:

```text
[0,0,1,1,2,2]
```

then:

```text
high = 3
```

`mid` stays at `2`.

---

now:

```text
nums[mid] = 1
```

so:

```text
mid += 1
```

now:

```text
mid = 3
```

again:

```text
nums[mid] = 1
```

so:

```text
mid += 1
```

now:

```text
mid = 4
high = 3
```

condition:

```python
mid <= high
```

is false.

so we stop.

final array:

```text
[0,0,1,1,2,2]
```

---

# IMPORTANT POINTS -

### 1. `low`

`low` tells us where the next `0` should be placed.

```text
0s are on the left side
```

### 2. `mid`

`mid` is the **current element we are checking**.

### 3. `high`

`high` tells us where the next `2` should be placed.

```text
2s are on the right side
```

### 4. why don't we increase `mid` when we find `2`?

because after swapping:

```python
nums[mid], nums[high] = nums[high], nums[mid]
```

the new value at `mid` is still unknown.

so we check it again.

### 5. this is done in-place

we are directly modifying:

```python
nums
```

instead of creating another array.

---

# TIME COMPLEXITY -

```text
O(n)
```

we go through the array only once.

each element is processed a limited number of times.

---

# SPACE COMPLEXITY -

```text
O(1)
```

we only use three variables:

```text
low
mid
high
```

no extra array is created.

---

# FINAL IDEA -

the whole algorithm can be remembered like this:

```text
0 -> move to low
1 -> leave it, move mid
2 -> move to high, check mid again
```

or simply:

```text
0 -> LEFT
1 -> MIDDLE
2 -> RIGHT
```

