class Solution:
    def myAtoi(self, s: str) -> int:
        temp = []
        intVal = ["0","1","2","3","4","5","6","7","8","9"]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        i = 0

        while i < len(s):
            if s[i] == " " and not temp:
                i += 1
                continue

            elif (s[i] == "+" or s[i] == "-") and not temp:
                temp.append(s[i])
                i += 1
                continue

            elif s[i] == "+" or s[i] == "-":
                break

            elif s[i] in intVal:
                temp.append(s[i])
            else:
                break

            i += 1

        if not temp or temp == ["+"] or temp == ["-"]:
            return 0

        num = int(''.join(temp))

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
