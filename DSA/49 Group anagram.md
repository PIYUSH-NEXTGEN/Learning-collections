<img width="1916" height="786" alt="image" src="https://github.com/user-attachments/assets/4606d963-7a86-468d-86aa-d0e3c8783ea9" />


```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
```

# PROBLEM

so in the ques we have given an array of strings `strs` and we have to group all the anagrams together.

two strings are anagrams if they contain the same characters with the same frequency, but the order of the characters can be different.

we have to return a list where each group contains strings that are anagrams of each other.

like here:

`strs = ["eat","tea","tan","ate","nat","bat"]`

here:

`"eat"`, `"tea"` and `"ate"` are anagrams because they contain the same characters:

`e -> 1`

`t -> 1`

`a -> 1`

similarly:

`"tan"` and `"nat"` are anagrams because they contain:

`t -> 1`

`a -> 1`

`n -> 1`

and `"bat"` does not have any other anagram in the array.

therefore the answer will be:

```python
[["eat","tea","ate"],["tan","nat"],["bat"]]
```

# APPROACH

so here we use a dictionary to store different groups of anagrams.

the main idea is that if two strings are anagrams, their character frequencies will be exactly the same.

for example:

```text
eat
tea
ate
```

all three strings have:

```text
a -> 1
e -> 1
t -> 1
```

so instead of sorting every string, we create a **frequency count of all 26 lowercase English characters**.

we create:

```python
count = [0] * 26
```

this creates an array of 26 zeros.

each position represents one character:

```text
index 0  -> a
index 1  -> b
index 2  -> c
...
index 25 -> z
```

then for every character in the string, we increase its corresponding count.

for example:

```text
s = "eat"
```

the count will represent:

```text
a -> 1
e -> 1
t -> 1
```

then we convert this count list into a tuple:

```python
key = tuple(count)
```

we use this tuple as the key of our dictionary.

the important thing is that **anagrams will always produce the same key**.

for example:

```text
eat -> same frequency key
tea -> same frequency key
ate -> same frequency key
```

so they will all be stored inside the same group.

we check:

```python
if key not in groups:
    groups[key] = []
```

this means if we haven't seen this particular character frequency before, we create an empty list for that group.

then:

```python
groups[key].append(s)
```

adds the current string to its anagram group.

at the end:

```python
return list(groups.values())
```

returns all the groups stored inside the dictionary.

# CODE EXPLAINATION

```python
groups = {}
```

we create an empty dictionary to store the groups of anagrams.

the **key** will represent the character frequency of a string.

the **value** will be a list containing all strings having that same character frequency.

for example:

```python
{
    (1, 0, 0, 0, 1, ...): ["eat", "tea", "ate"]
}
```

---

```python
for s in strs:
```

this loop goes through every string in the `strs` array one by one.

for example:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

the value of `s` will be:

```text
eat
tea
tan
ate
nat
bat
```

one by one.

---

```python
count = [0] * 26
```

for every new string, we create a new array of 26 zeros.

each index represents a lowercase English character.

```text
0 -> a
1 -> b
2 -> c
...
25 -> z
```

this array will be used to count how many times each character appears in the string.

---

```python
for c in s:
```

this loop goes through every character of the current string.

for example, if:

```python
s = "eat"
```

then:

```text
c = e
c = a
c = t
```

---

```python
count[ord(c) - ord('a')] += 1
```

this is used to find the correct index for each character.

`ord()` gives us the ASCII/Unicode value of a character.

for example:

```python
ord('a') = 97
ord('b') = 98
ord('c') = 99
```

so:

```python
ord('e') - ord('a')
```

becomes:

```text
101 - 97 = 4
```

therefore `e` is stored at index `4`.

similarly:

```text
a -> 0
b -> 1
c -> 2
d -> 3
e -> 4
...
t -> 19
```

so for:

```text
"eat"
```

the characters will increase these positions:

```text
a -> count[0]  = 1
e -> count[4]  = 1
t -> count[19] = 1
```

---

```python
key = tuple(count)
```

we convert the `count` list into a tuple.

we do this because we want to use the character frequency as a **dictionary key**.

lists cannot be used as dictionary keys because lists are mutable.

tuples can be used as dictionary keys because they are immutable.

so now the frequency array becomes our unique key for the anagram group.

for example:

```text
eat -> [1,0,0,0,1,...,1,...]
tea -> [1,0,0,0,1,...,1,...]
ate -> [1,0,0,0,1,...,1,...]
```

all three strings produce the same key.

---

```python
if key not in groups:
    groups[key] = []
```

we check whether this character-frequency key already exists in the dictionary.

if it does not exist, we create a new empty list for it.

for example, when we first see:

```text
eat
```

there is no matching key, so we create a new group:

```python
groups[key] = []
```

---

```python
groups[key].append(s)
```

we add the current string to the group represented by that key.

so after processing `"eat"`:

```python
["eat"]
```

when we process `"tea"`, it produces the same key, so it gets added to the same group:

```python
["eat", "tea"]
```

then `"ate"` also produces the same key:

```python
["eat", "tea", "ate"]
```

---

```python
return list(groups.values())
```

finally, we return all the values of the dictionary.

the dictionary contains the anagram groups, but we only need the groups themselves, not their keys.

so we use:

```python
groups.values()
```

and convert it into a list:

```python
list(groups.values())
```

for:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

the result will be:

```python
[["eat","tea","ate"],["tan","nat"],["bat"]]
```

# EXAMPLE

let's take:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

first:

```text
s = "eat"
```

frequency:

```text
a -> 1
e -> 1
t -> 1
```

we create a key for this frequency and store:

```text
["eat"]
```

then:

```text
s = "tea"
```

it has the same character frequencies:

```text
a -> 1
e -> 1
t -> 1
```

so it gets the same key.

now the group becomes:

```text
["eat", "tea"]
```

then:

```text
s = "tan"
```

its frequency is:

```text
a -> 1
n -> 1
t -> 1
```

this is a different key, so a new group is created:

```text
["tan"]
```

then:

```text
s = "ate"
```

it has the same frequency as `"eat"` and `"tea"`:

```text
a -> 1
e -> 1
t -> 1
```

so it is added to the first group:

```text
["eat", "tea", "ate"]
```

then `"nat"` has the same frequency as `"tan"`:

```text
a -> 1
n -> 1
t -> 1
```

so:

```text
["tan", "nat"]
```

finally `"bat"` has a different frequency, so it gets its own group:

```text
["bat"]
```

therefore the final answer is:

```python
[["eat","tea","ate"],["tan","nat"],["bat"]]
```

# TIME COMPLEXITY

let:

* `n` = number of strings
* `k` = maximum length of a string

for every string, we go through all of its characters.

so the time complexity is:

```text
O(n * k)
```

we do not sort the strings, so we avoid the `O(k log k)` sorting cost.

# SPACE COMPLEXITY

we store the character-frequency key and the groups inside the dictionary.

the space complexity is:

```text
O(n * k)
```

because we store all the strings in the groups.

the `count` array itself always has only 26 elements, so its size is effectively constant:

```text
O(26) = O(1)
```
