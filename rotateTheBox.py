class Solution:
    def rotateTheBox(self, arr: List[List[str]]) -> List[List[str]]:
        n = len(arr)
        m = len(arr[0])
        ans = []
        for i in range(n):
            if '*' not in arr[i]:
                    arr[i].sort(reverse = True)
                    continue
            a = -1
            temp = []
            for j in range(m):
                if arr[i][j] == '*':
                    temp += sorted(arr[i][a+1:j],reverse = True)+['*']
                    a = j
            temp+=sorted(arr[i][a+1:],reverse=True)
            arr[i]=temp
        print(arr)
        
        for i in range(m):
            temp = []
            for j in range(n-1,-1,-1):
                temp.append(arr[j][i])
            ans.append(temp)
        return ans    
