<img width="1919" height="783" alt="image" src="https://github.com/user-attachments/assets/96a89709-b588-4c44-ada2-e91dbce6e576" />

# DESIGN HASHSET

## Problem

so in the ques we have to design our own `HashSet`.

we need to implement 3 functions:

* `add(key)` -> adds the key to the set
* `remove(key)` -> removes the key from the set
* `contains(key)` -> checks if the key exists in the set

the main point is that we should not use Python's built-in `set`.

---

## Approach

so here we use a **hashing technique**.

we create:

```python
self.size = 1000
self.bucket = [ [] for i in range(self.size)]
```

here we create `1000` buckets.

each bucket is a list, so if multiple keys get the same index, we can store them together in that list.

to decide which bucket a key belongs to, we use:

```python
index = key % self.size
```

this gives us an index between `0` and `999`.

for example:

```text
key = 15

15 % 1000 = 15

so key 15 goes to bucket[15]
```

another example:

```text
key = 1015

1015 % 1000 = 15

so key 1015 also goes to bucket[15]
```

this is called a **collision**.

because both keys get the same index, we store both of them inside the same bucket.

---

## Code Explanation

### 1. `__init__`

```python
def __init__(self):
    self.size = 1000
    self.bucket = [ [] for i in range(self.size)]
```

first we set the size of our hashset:

```python
self.size = 1000
```

then we create `1000` empty lists:

```python
self.bucket = [ [] for i in range(self.size)]
```

so basically it looks like:

```text
bucket[0]  -> []
bucket[1]  -> []
bucket[2]  -> []
...
bucket[999] -> []
```

these lists are used to store the keys.

---

### 2. `add`

```python
def add(self, key: int) -> None:
    index = key % self.size

    if key not in self.bucket[index]:
        self.bucket[index].append(key)
```

first we find where the key should be stored:

```python
index = key % self.size
```

for example:

```text
key = 25

25 % 1000 = 25
```

so we use:

```python
bucket[25]
```

then we check:

```python
if key not in self.bucket[index]:
```

this makes sure we don't add the same key twice.

if the key is not already there:

```python
self.bucket[index].append(key)
```

we add it to that bucket.

---

### 3. `remove`

```python
def remove(self, key: int) -> None:
    index = key % self.size

    if key in self.bucket[index]:
        self.bucket[index].remove(key)
```

again we calculate the bucket:

```python
index = key % self.size
```

then we check if the key exists in that bucket:

```python
if key in self.bucket[index]:
```

if it exists, we remove it:

```python
self.bucket[index].remove(key)
```

if the key doesn't exist, nothing happens.

---

### 4. `contains`

```python
def contains(self, key: int) -> bool:
    index = key % self.size
    return key in self.bucket[index]
```

first we find the bucket:

```python
index = key % self.size
```

then:

```python
return key in self.bucket[index]
```

checks whether the key exists inside that bucket.

it returns:

```text
True  -> key exists
False -> key does not exist
```

---

## Example

suppose we do:

```python
add(1)
add(1001)
add(2)
```

for `1`:

```text
1 % 1000 = 1

bucket[1] -> [1]
```

for `1001`:

```text
1001 % 1000 = 1

bucket[1] -> [1, 1001]
```

so both keys are stored in the same bucket because they have the same index.

then:

```python
contains(1001)
```

checks:

```text
1001 % 1000 = 1
```

then looks inside:

```text
bucket[1] -> [1, 1001]
```

`1001` is present, so it returns:

```text
True
```

if we do:

```python
remove(1)
```

then:

```text
bucket[1] -> [1001]
```

so `1` is removed but `1001` is still there.

---

## Important Point

the important thing here is the `%` operator:

```python
index = key % self.size
```

it converts a large key into a valid bucket index.

and the bucket itself is a list because **different keys can have the same index**.

this is how we handle collisions.

```text
key
 ↓
key % 1000
 ↓
bucket index
 ↓
search inside that bucket
```

---

## Time Complexity

average case:

```text
add      -> O(1)
remove   -> O(1)
contains -> O(1)
```

because we directly find the bucket using `%`.

technically, because each bucket is a list, a collision can make the operation slower if many keys land in the same bucket.

---

## Space Complexity

```text
O(n)
```

where `n` is the number of keys stored in the HashSet.

we also have `1000` buckets, but the main extra space depends on the number of stored keys.
