<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/17ee82de-6741-4312-b2cb-1ee0b8407fdb" />


# MAJORITY ELEMENT

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums) // 2

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

            if hashmap[i] > n:
                return i
```

# PROBLEM

so in the ques we have given an array `nums` and we have to find the **majority element**.

the majority element is the element that appears **more than `n / 2` times** in the array.

here `n` is the length of the array.

we have to return that element.

like here:

```python
nums = [2,2,1,1,1,2,2]
```

the length of the array is:

```text
n = 7
```

so the majority element must appear more than:

```text
7 / 2 = 3.5
```

times.

here `2` appears `4` times:

```text
2 -> 4 times
1 -> 3 times
```

since `2` appears more than `3.5` times, `2` is the majority element.

therefore the answer will be:

```text
2
```

# APPROACH

so here we use a **hashmap (dictionary)** to keep track of how many times each element appears in the array.

first we create an empty dictionary:

```python
hashmap = {}
```

then we calculate half of the length of the array:

```python
n = len(nums) // 2
```

we do this because the majority element must appear **more than `n / 2` times**.

then we loop through every element in the array:

```python
for i in nums:
```

for every element, we increase its count in the hashmap.

we use:

```python
hashmap[i] = hashmap.get(i, 0) + 1
```

this means:

* if `i` is already present in the hashmap, get its current count.
* if `i` is not present, use `0`.
* then add `1` to the count.

after increasing the count, we check:

```python
if hashmap[i] > n:
```

this checks if the current element has appeared more than half of the array length.

if it has, we know that it is the majority element, so we return it:

```python
return i
```

for example:

```python
nums = [2,2,1,1,1,2,2]
```

the length is `7`.

so:

```python
n = 7 // 2
n = 3
```

the majority element must appear more than `3` times.

when we reach the fourth `2`:

```text
2 -> 4 times
```

we check:

```text
4 > 3
```

this is true.

so we return:

```text
2
```

# CODE EXPLAINATION

```python
hashmap = {}
```

we create an empty dictionary.

this dictionary will store each element as a key and its frequency as the value.

for example, after processing some elements, it can look like:

```python
{
    2: 3,
    1: 2
}
```

this means:

```text
2 -> appears 3 times
1 -> appears 2 times
```

---

```python
n = len(nums) // 2
```

first we find the length of the array and divide it by `2`.

we use integer division `//`.

for example:

```python
nums = [2,2,1,1,1,2,2]
```

the length is:

```text
7
```

so:

```python
n = 7 // 2
```

which gives:

```text
n = 3
```

the majority element needs to appear **more than 3 times**.

---

```python
for i in nums:
```

this loop goes through every element of the array one by one.

for:

```python
nums = [2,2,1,1,1,2,2]
```

the value of `i` will be:

```text
2
2
1
1
1
2
2
```

one by one.

---

```python
hashmap[i] = hashmap.get(i, 0) + 1
```

this line counts how many times the current element has appeared.

`hashmap.get(i, 0)` means:

if `i` already exists in the hashmap, get its current count.

if `i` does not exist, return `0`.

then we add `1`.

for example, when we see `2` for the first time:

```python
hashmap.get(2, 0)
```

because `2` is not in the hashmap, it returns:

```text
0
```

then:

```text
0 + 1 = 1
```

so:

```python
hashmap = {
    2: 1
}
```

when we see `2` again:

```text
current count = 1
```

then:

```text
1 + 1 = 2
```

so:

```python
hashmap = {
    2: 2
}
```

and this continues every time we see `2`.

---

```python
if hashmap[i] > n:
```

after increasing the count, we check if the current element has appeared more than half of the array length.

remember:

```text
majority element -> appears more than n / 2 times
```

we already calculated:

```python
n = len(nums) // 2
```

so now we simply check:

```python
hashmap[i] > n
```

for example, if:

```text
n = 3
```

then we need:

```text
count > 3
```

so:

```text
count = 4
```

means the element is the majority element.

---

```python
return i
```

if the count is greater than `n`, we have found the majority element.

so we return the current element `i`.

# EXAMPLE

let's take:

```python
nums = [2,2,1,1,1,2,2]
```

first:

```python
n = len(nums) // 2
```

so:

```text
n = 7 // 2
n = 3
```

now we start the loop.

### First element

```text
i = 2
```

`2` is not in the hashmap.

so:

```text
2 -> 1
```

we check:

```text
1 > 3
```

false.

---

### Second element

```text
i = 2
```

`2` already exists.

so its count becomes:

```text
2 -> 2
```

we check:

```text
2 > 3
```

false.

---

### Third element

```text
i = 1
```

`1` is not in the hashmap.

so:

```text
1 -> 1
```

we check:

```text
1 > 3
```

false.

---

### Fourth element

```text
i = 1
```

its count becomes:

```text
1 -> 2
```

we check:

```text
2 > 3
```

false.

---

### Fifth element

```text
i = 1
```

its count becomes:

```text
1 -> 3
```

we check:

```text
3 > 3
```

false.

---

### Sixth element

```text
i = 2
```

its count becomes:

```text
2 -> 3
```

we check:

```text
3 > 3
```

false.

---

### Seventh element

```text
i = 2
```

its count becomes:

```text
2 -> 4
```

we check:

```text
4 > 3
```

true.

so we return:

```python
2
```

therefore the final answer is:

```text
2
```

# IMPORTANT POINT

we use `>` and not `>=`.

this is because the question says the majority element appears **more than `n / 2` times**.

for example, if:

```text
n = 6
```

then:

```text
n / 2 = 3
```

an element appearing exactly `3` times is **not** a majority element.

it must appear:

```text
more than 3
```

so it needs to appear at least `4` times.

that's why we use:

```python
if hashmap[i] > n:
```

# TIME COMPLEXITY

we go through the array once.

for every element, hashmap insertion and lookup takes `O(1)` average time.

therefore the time complexity is:

```text
O(n)
```

where `n` is the number of elements in the array.

# SPACE COMPLEXITY

we use a hashmap to store the frequency of elements.

in the worst case, every element can be different, so the hashmap can contain `n` different elements.

therefore the space complexity is:

```text
O(n)
```


        
