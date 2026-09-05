<img width="1919" height="791" alt="image" src="https://github.com/user-attachments/assets/c1805c01-bf56-423c-b3d0-94b7ad175420" />

# DESIGN HASHMAP

```python
class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
```

# PROBLEM -

the question is simple, we have to make a hashmap but without using the built-in hashmap/dictionary.

in the hashmap we can do:

* `put` -> insert a key and its value
* `get` -> return the value of the key. if that key doesn't exist, return `-1`
* `remove` -> remove the key and its value from the hashmap

---

# APPROACH -

we will use **linked list** to implement the hashmap.

first, in another class `ListNode`, we will store:

* `key`
* `value`
* `next` node

then in the `MyHashMap` class, we will create **1000 dummy nodes**.

```python
self.map = [ListNode() for _ in range(1000)]
```

so basically every index of `self.map` will have one dummy node.

for example:

```text
bucket[0] -> [-1, -1] -> None
bucket[1] -> [-1, -1] -> None
bucket[2] -> [-1, -1] -> None
```

`key = -1` and `val = -1` are just the default values of the dummy nodes.

---

## HASH FUNCTION -

for hash we will do:

```python
key % len(self.map)
```

this will give us the **index** where we need to search/store the key.

for example:

```text
key = 5

5 % 1000 = 5
```

so `5` is the **index**, not the key.

another example:

```text
key = 1005

1005 % 1000 = 5
```

here also the index is `5`.

this means both `5` and `1005` will go to the same bucket.

this is called a **collision**.

that's why we use a linked list inside every bucket.

---

# PUT -

in the `put` function:

```python
cur = self.map[self.hash(key)]
```

here:

```text
self.hash(key)
```

calculates the index.

for example:

```text
key = 5

5 % 1000 = 5
```

so:

```python
self.map[5]
```

gets the dummy node at index `5`.

therefore:

```python
cur = self.map[self.hash(key)]
```

means `cur` is now pointing to the dummy node of that bucket.

then:

```python
while cur.next:
```

we move through the linked list as long as there is another node.

then:

```python
if cur.next.key == key:
```

we check if the key already exists.

if the key already exists:

```python
cur.next.val = value
```

we update its value.

then:

```python
return
```

because we don't need to add a new node.

if the key doesn't exist, we move to the next node:

```python
cur = cur.next
```

and continue checking.

after the loop finishes, it means the key doesn't exist in that bucket.

so we create a new node:

```python
cur.next = ListNode(key, value)
```

and add it at the end of the linked list.

---

# GET -

in the `get` function:

```python
cur = self.map[self.hash(key)].next
```

first we find the correct bucket using the hash function.

but here we use `.next` because we don't want to start from the dummy node.

we want to start from the first actual key-value node.

then:

```python
while cur:
```

we go through the linked list.

if the key exists:

```python
if cur.key == key:
    return cur.val
```

we return the **value** of that key.

for example:

```text
key = 5
value = 100
```

then:

```python
get(5)
```

will return:

```text
100
```

if we reach the end of the linked list and don't find the key:

```python
return -1
```

---

# REMOVE -

in the `remove` function:

```python
cur = self.map[self.hash(key)]
```

again we first find the correct bucket.

here we start from the dummy node because we need to modify the `next` pointer when removing a node.

then:

```python
while cur.next:
```

we check the nodes in the linked list.

if the key exists:

```python
if cur.next.key == key:
```

then:

```python
cur.next = cur.next.next
```

this basically skips the node we want to remove.

for example:

```text
cur -> A -> B -> C
```

if `B` is the node we want to remove:

```text
cur -> A -> C
```

because:

```python
cur.next = cur.next.next
```

makes `A` directly point to `C`.

then we use:

```python
return
```

because the key has been removed.

if the key is not found, nothing happens.

---

# IMPORTANT POINT -

the main idea is:

```text
key
 ↓
hash function
 ↓
index
 ↓
bucket
 ↓
linked list
```

we use multiple buckets so we can quickly find where a key should be.

and if two keys get the same index, we store them in the same bucket using a linked list.

for example:

```text
5 % 1000 = 5
1005 % 1000 = 5
2005 % 1000 = 5
```

so:

```text
bucket[5]

dummy -> [5, 100] -> [1005, 200] -> [2005, 300]
```

this is how we handle **collisions**.

---

# TIME COMPLEXITY -

average case:

```text
put    -> O(1)
get    -> O(1)
remove -> O(1)
```

because we use the hash function to directly find the bucket.

but if many keys have the same index, we have to search through the linked list, so in the worst case it can become:

```text
O(n)
```

# SPACE COMPLEXITY -

```text
O(n)
```

where `n` is the number of key-value pairs stored in the hashmap.

