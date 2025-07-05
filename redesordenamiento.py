a = [3,2,4,1]

def inter(arr, i1,i2):
    if arr[i1] > arr[i2]:
        arr[i1], arr[i2] = arr[i2], arr[i1]

def redorden4(arr):
    inter(arr, 0,2)
    inter(arr, 1,3)
    inter(arr, 0,1)
    inter(arr, 2,3)
    inter(arr, 1,2)
    

print(a)
redorden4(a)
print(a)
