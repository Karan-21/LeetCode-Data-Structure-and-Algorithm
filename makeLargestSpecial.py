class Solution:
    def makeLargestSpecial(self, binString):
        counter = secondCounter = 0
        res = []
        for j, v in enumerate(binString):
            counter = counter + 1 if v == '1' else counter - 1
            if counter == 0:
                res.append(
                    '1' + self.makeLargestSpecial(binString[secondCounter + 1:j]) + '0')
                secondCounter = j + 1
        return ''.join(sorted(res)[::-1])
