class Solution:
    def survivedRobotsHealths(self, pos: List[int], heal: List[int], drct: str) -> List[int]:
        stk,spos = [], sorted(range(len(pos)), key=lambda i: pos[i])
        for i in spos:
            if  drct[i] == 'R':  stk.append(i)
            else:
                while stk and heal[i] > heal[stk[-1]]: heal[stk.pop()] = 0; heal[i] -= 1
                if    stk and heal[i]== heal[stk[-1]]: heal[stk.pop()] = 0; heal[i]  = 0
                elif  stk:                             heal[stk[-1]]  -= 1; heal[i]  = 0
        return [h for h in heal if h>0]
        
