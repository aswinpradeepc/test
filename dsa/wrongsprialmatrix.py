class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        flows = min(m,n) + min(m,n)-1
        flowControl = list('RDLU')
        i = 0
        resControl = []
        while i < flows:
            resControl.append(flowControl[i%4])
            i += 1
        resIndex =[]
        r=0
        d=0
        l=0
        u=0
        for index,item  in enumerate(resControl):
            if item == 'R':
                count = n - r
                j = r
                while j<count:
                    resIndex.append([r,j])
                    j+=1
                r+=1
            elif item == 'D':
                count = m - d
                const = m - d -1
                for j in range(d+1,count):
                    resIndex.append([j,const])
                d+=1
            elif item == 'L':
                const = n - l -1
                count = n - l*2 - 1
                start = n - l - 2
                for j in range(count,0, -1):
                    resIndex.append([const,start])
                    start -=1
                l+=1
            elif item == 'U':
                const = u
                count = m - (u+1)*2
                for j in range (count,0,-1):
                    resIndex.append([j,u])
                u+=1
        result = []
        for i in resIndex:
            p=int(i[0])
            q=int(i[1])
            result.append(matrix[p][q])
        return result