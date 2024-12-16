nas =[9,7,5,4,3,1,6,99]
def bubbleSort(numArr):
    n = len(numArr)
    for i in range (0,n):
        for j in range(0,n-i-1):
            if numArr[j]>numArr[j+1]:
                temp = numArr[j]
                numArr[j]=numArr[j+1]
                numArr[j+1]=temp
    print(numArr)
bubbleSort(nas)
