class Solution(object):
    def romanToInt(self, s):
        # Словарь для сопоставления римских символов с их значениями
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

        # Инициализация переменной для хранения результата
        num = 0

       # Итерация по строке с римским числом
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                num += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1

        return num

solution = Solution()
result = solution.romanToInt("C")
print(result)  
