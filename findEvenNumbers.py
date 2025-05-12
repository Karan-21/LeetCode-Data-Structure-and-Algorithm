class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        for i in range(100, 1000, 2):
            temp = str(i)
            for j in temp:
                if int(j) in digits:
                    if temp.count(j) > digits.count(int(j)):
                        break
                else:
                    break
            else:
                result.append(i)
        return result
