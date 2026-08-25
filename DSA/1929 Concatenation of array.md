<img width="1919" height="719" alt="image" src="https://github.com/user-attachments/assets/fbca5d4d-bbc9-428f-9a75-3d68d2b2e3d7" />

```
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(i)

        ans += nums

        return ans
  ```
