def min_binary(arr, target):
    high = len(arr)
    low = 0
    mid = int((low + high) / 2)

    while high >= low:
        print("{} {} {}".format(low, mid, high))
        if mid >= len(arr):
            return len(arr)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = int((low + high) / 2)
    if arr[low] != target: return low - 1
    return low

def max_binary(arr, target):
    high = len(arr) - 1
    low = 0
    mid = int((low + high) / 2)

    while high >= low:
        if mid >= len(arr):
            return len(arr)
        elif arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
        mid = int((low + high) / 2)
    if arr[high] != target: return high + 1
    return high

def test_min_binary():
    assert min_binary([1,1,1], 1) == 0
    assert min_binary([1,1,1,1], 1) == 0
    assert min_binary([1,1,1], 0) == -1
    assert min_binary([1,1,1], 2) == 3
    assert min_binary([0,1,2,2,2,3,4,5,9,9], 9) == 8
    assert min_binary([0,1,2,2,2,3,4,5,9,9], 2) == 2
    assert min_binary([0,2,2,2,3,4,5,9,9], 1) == 0
    assert min_binary([0,2,2,2,3,4,5,9,9], 4.5) == 5

def test_max_binary():
    assert max_binary([1,1,1], 1) == 2
    assert max_binary([1,1,1], 0) == 0
    assert max_binary([1,1,1], 2) == 3
    assert max_binary([0,1,2,2,2,3,4,5,9,9], 9) == 9
    assert max_binary([0,1,2,2,2,3,4,5,9,9], 2) == 4
    assert max_binary([0,1,2,2,2,3,4,5,9,9], 10) == 10
    assert max_binary([0,1,2,2,2,3,4,5,9,9], 2.5) == 5
    assert max_binary([0,1,2,2,2,3,4,5,9,9], 4.5) == 7

test_min_binary()
test_max_binary()
print("All tests passed :)")

