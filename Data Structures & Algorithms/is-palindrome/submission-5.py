class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for i in s:
            if i.isalnum():
                clean += i.lower()
        a = 0
        b = len(clean)-1
        res = True

        while a < b:
            if clean[a] != clean[b]:
                    return False
                    break
            a += 1
            b -= 1

        return res