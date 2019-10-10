def sort(arr, leftBorder, rightBorder):
    if leftBorder < rightBorder:
        tmp = leftBorder - 1
        pivot = arr[rightBorder]
        for i in range(leftBorder, rightBorder):
            if arr[i] < pivot:
                tmp += 1
                arr[tmp], arr[i] = arr[i], arr[tmp]
        arr[tmp + 1], arr[rightBorder] = arr[rightBorder], arr[tmp + 1]
        tmp += 1
        sort(arr, leftBorder, tmp - 1)
        sort(arr, tmp + 1, rightBorder)

if __name__ == "__main__":
    print("Input:")
    n = int(input())
    array = list(map(int, input().split(' ')))
    m = 0
    for i in range(n):
        if array[i] % 3 == 0:
            array[i], array[m] = array[m], array[i]
            m += 1
    sort(array, 0, m - 1)
    sort(array, m, n - 1)
    print("Output:")
    for i in range(n):
        print(array[i], end=" ")
