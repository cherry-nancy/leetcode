
>>> class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(min(numRows, len(s)))]
        curRow = 0
        goingdown = False
        
        for c in s:
            rows[curRow].append(c)
            if (curRow == 0 or curRow == numRows -1) :
                goingdown =  not goingdown
            if goingdown:
                curRow += 1
            else: curRow -= 1
        res = [''.join(i) for i in rows]
        return ''.join(res)
            