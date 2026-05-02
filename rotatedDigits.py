class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        def isGood(num):
            string = str(num)
            newNum = ""
            for i in range(len(string)):
                if string[i] == "3" or string[i] == "4" or string[i] == "7":
                    return False
                if string[i] == "0" or string[i] == "1" or string[i] == "8":
                    newNum += string[i]
                if string[i] == "2":
                    newNum += "5"
                if string[i] == "5":
                    newNum += "2"
                if string[i] == "6":
                    newNum += "9"
                if string[i] == "9":
                    newNum += "6"
            if newNum == string: return False
            return True
        for i in range(1, n + 1):
            if isGood(i):
                count += 1
        return count
