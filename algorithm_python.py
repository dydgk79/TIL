# 2025.02.05~2025.02.10

# 배열
## 알고리즘 풀이할 때 인풋 받는 예시
"""
T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split))
    print(f'{test_case}')
"""

# 정렬

## 버블
# 밑에서부터 교환식으로 정렬하며 올라오는게 거품같다하여 버블 정렬
# 시간복잡도 : O(n^2)
arr = [1, 7, 5, 3, 5, 8, 9, 6]
# 내 구현
for i in range(len(arr)):
    for j in range(i, len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
# 교재 구현
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] - a[j+1], a[j]


## 카운팅 정렬
# 리스트에 있는 숫자들의 수를 세어 뒤에서부터 붙이는 식으로 정렬
# 한정된 상황에서 빠르게 정렬 가능
# 시간복잡도 : O(n+k), k는 정수의 최댓값
def counting_sort(data, temp, k):
    # data : 입력 배열, temp : 정렬된 배열, counts : 카운트 배열
    counts = [0] * (k+1)
    for i in range(len(data)):
        counts[data[i]] += 1
    for i in range(1, k+1):
        counts[i] += counts[i-1]
    for i in range(len(data-1, -1, -1)):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]


# 완전검색
# 순열
# 탐욕 알고리즘 : 일반적으로 딱 눈에 보이자마자 풀리는 방법
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해
# 나가는 방식으로 진행하여 최종적인 해답에 도달


# 2차원 배열

# arr = [list(map(int, input().split())) for _ in range(N)]
N = 3
arr = [[0]*N for _ in range(N)]

# 델타를 활용한 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < N:
                # print(ni, nj)
                pass

# 부분집합
# 있냐, 없냐를 1과 0으로 표현하여 부분집합 구현
# 비트연산자 사용
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            # 부분집합 원소로 포함됨
            pass


# 검색

# 순차 검색
# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# 알고리즘 단순해서 구현 쉽지만, 항목이 많아지면 오래걸린다.
# 시간 복잡도 : O(n)
def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1

def seq_search_2d(arr, n, key):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == key:
                return i, j
    return 0

# 정렬되어 있는 경우, 실패의 상황임을 빨리 알 수 있으므로 더 빨리 동작할 수 있다.
def seq_search_sort(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:
            return -1
    return -1


# 이진 검색
# 정렬되어 있는 자료, 절반으로 잘라 확인하고 찾는 구역을 줄이고 다시 반으로 갈라 찾는 방식
def binary_search(a, n, key):
    start = 0
    end = n-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle +1
    return -1

# 선택 정렬
# 자료의 최솟값을 찾아 그 부분의 인덱스를 저장하고, 그 최솟값을 제일 앞의 값과 바꾸는 정렬
# 버블은 다음것과 비교하여 교환하는 정렬 방식이고,
# 선택정렬은 최솟값(최댓값)을 찾아 맨 앞의 자료와 바꾸는 것이다.
def selection_sort(a, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

# String

## 문자열 뒤집기

## 문자열 연산

## for-else

## 패턴 매칭

## KMP 알고리즘

## 보이어-무어


# Stack

## 스택

## 괄호 검사, function call

## 재귀귀