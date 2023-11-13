import json

arr1 = []
def jsonLoader():
    f = open("index.json", "r")
    num1 = json.load(f)
    for x in range(len(num1["arr"])):
        arr1.append(num1["arr"][x])
    f.close()
jsonLoader()
arr2 = []
def sorting():
    for x in range(len(arr1)): 
        arr2.append(min(arr1))
        arr1.remove(min(arr1))
sorting()
arr3 = []
def plusorminus():
    targetPlus = 0
    targetTimes = 1
    index1 = 0
    index2 = 1
    for x in range(len(arr2)):
        if (x == index1): 
            targetPlus += arr2[index1]
            index1 += 2
        elif (x == index2):
            targetTimes *= arr2[index2]
            index2 += 2
    arr3.append(targetPlus)
    arr3.append(targetTimes)
plusorminus()
def files():
    f = open("nums.txt", "a")
    for x in range(len(arr3)): 
        f.write(str(arr3[x]))
        f.write("\n")
    f.close()
files()