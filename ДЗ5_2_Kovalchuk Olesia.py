def bound(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return iterations, arr[mid]

    if low <= len(arr) - 1:
        return iterations, arr[low]
    else:
        return iterations, arr[high] if high >= 0 else None

arr = [1.2, 2.0, 2.6, 3.3, 4.2, 5.6]
x_values = [1.0, 4.0]

for x in x_values:
    result = bound(arr, x)

    if result[1] is not None:
        print(f"Результат для {x}: (кількість ітерацій, {result[1]})")
    else:
        print(f"Результат для {x}: (кількість ітерацій, None)")
