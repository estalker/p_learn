class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.replace("  "," ")
        s.strip(" ")
        return " ".join(reversed(s.split()))



sol = Solution()
res = sol.reverseWords("hello  word  ");
print(res)