def max_area(arr):
    max_area = 0
    pair = None
    for a in enumerate(arr, start=1):
        for b in enumerate(arr[a[0]:], start=a[0]+1):
            area = (b[0] - a[0]) * min(a[1], b[1])
            if area > max_area:
                max_area = area
                pair = (a, b)
    return pair, max_area


arr = [2, 7, 1, 7, 2, 1, 2]
print max_area(arr)

