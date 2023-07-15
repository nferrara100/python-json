class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "_": 0,
            "__": 0,
        }
        valueList = list(values)

        num = 0
        skip = False
        for index, character in enumerate(s):
            pos = valueList.index(character)
            num += values[character]
            if skip:
                num -= values[s[index - 1]] * 2
                skip = False
            if pos % 2 == 0 and len(s) > index + 1:
                if (
                    s[index + 1] == valueList[pos + 1]
                    or s[index + 1] == valueList[pos + 2]
                ):
                    skip = True
        return num


Solution().romanToInt("MCMXCIV")
