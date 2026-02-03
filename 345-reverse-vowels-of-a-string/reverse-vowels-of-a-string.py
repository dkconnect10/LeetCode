class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] not in vowels:
                i += 1
            elif chars[j] not in vowels:
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

        return "".join(chars)
