def maxheapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    while l < n and A[l] > A[largest]:
        largest = l
    while r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, n, largest)


def heapsort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        maxheapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        maxheapify(A, i, 0)


s = [15, 5, 20, 1, 17, 10, 30]
heapsort(s)
print(s)   