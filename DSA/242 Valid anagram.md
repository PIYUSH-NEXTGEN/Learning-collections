<img width="1919" height="693" alt="image" src="https://github.com/user-attachments/assets/dd6a6b87-5f45-4f05-b9ce-7fd987460614" />

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in s:
            if s.count(i) != t.count(i):
                return False

        return True
```

# PROBLEM

so in the ques we have given two strings s and t and we have to check if t is an anagram of s or not.

an anagram means both strings contain the same characters with the same frequency, but the order can be different.

like here s = "anagram" and t = "nagaram".

both strings have the same characters and the same number of each character, just their order is different, so the answer will be True.

but if s = "rat" and t = "car", the characters are different so the answer will be False.

# APPROACH

so here first we check the length of both strings.

if the length of s and t is different, then they cannot be anagrams because an anagram must contain the same number of characters, so we directly return False.

after that we loop through every character in s.

for every character we use count() to check how many times that character appears in s and how many times it appears in t.

if the count is different, it means both strings don't have the same frequency of that character, so we return False.

if every character has the same frequency in both strings, then they are anagrams and we return True.

CODE EXPLAINATION

```python
s = "anagram"

t = "nagaram"

if len(s) != len(t):  -> first checking if the length of both strings is different.
    return False         if the length is different, they cannot be anagrams, so we return False.

for i in s:  -> looping through every character of s.

for example, for s = "anagram" the loop will check a, n, a, g, r, a, m one by one.

if s.count(i) != t.count(i): -> checking how many times the current character i appears in both strings.
    return False

for example, for i = 'a':

s.count('a') = 3

t.count('a') = 3

so they are equal and we continue. if the count is different for any character, it means the strings are not anagrams, so we return False.

return True -> if the loop finishes without finding any character with a different frequency, it means both strings contain the same characters with the same frequency, so we return True.
```
