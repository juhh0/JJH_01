def selection_sort(data):
    comparisons, movements = 0, 0
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            movements += 2
    return data, comparisons, movements


def insertion_sort(data):
    n = len(data)  # 데이터의 길이를 저장
    comparisons, movements = 0, 0  # 비교 횟수와 이동 횟수를 초기화
    for i in range(1, n):
        key = data[i]  # 현재 삽입할 값을 키로 설정
        j = i - 1
        # 키보다 큰 요소들을 오른쪽으로 이동
        while j >= 0 and data[j] > key:
            comparisons += 1  # 비교 횟수 증가
            data[j + 1] = data[j]  # 요소를 오른쪽으로 이동
            movements += 1  # 이동 횟수 증가
            j -= 1
        # while 루프를 빠져나온 후 마지막으로 실패한 비교 횟수 증가
        if j >= 0:
            comparisons += 1
        # 키 값을 올바른 위치에 삽입
        data[j + 1] = key
        # 이동은 이미 while 루프에서 처리되었으므로 추가 이동 증가 없음
    return data, comparisons, movements  # 정렬된 데이터와 비교/이동 횟수를 반환


def bubble_sort(data):
    comparisons, movements = 0, 0
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                movements += 2
    return data, comparisons, movements

def shell_sort(data):
    """
    셸 정렬 구현: 주어진 간격(gap)으로 배열을 나누고, 각 부분 배열에 대해 삽입 정렬 수행.
    """
    n = len(data)
    gap = n // 2  # 초기 간격 설정

    # 비교와 이동 횟수 추적
    comparisons = 0
    movements = 0

    while gap > 0:

        # 간격을 기준으로 삽입 정렬 수행
        for start in range(gap):  # 각 부분 배열 시작점
            # 삽입 정렬 수행
            for i in range(start + gap, n, gap):
                key = data[i]
                j = i - gap

                # 삽입 정렬의 비교 및 이동 수행
                while j >= start and data[j] > key:
                    comparisons += 1  # 비교 증가
                    data[j + gap] = data[j]
                    movements += 1  # 이동 증가
                    j -= gap

                # 마지막 비교 수행
                if j >= start:
                    comparisons += 1  # 실패한 비교

                # 올바른 위치에 삽입
                data[j + gap] = key
                movements += 1  # 이동 증가

        # 간격을 절반으로 줄임
        gap //= 2

    return data, comparisons, movements



def heapify(data, n, i, metrics):
    comparisons, movements = metrics
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons += 1
        if data[left] > data[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if data[right] > data[largest]:
            largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        movements += 2
        data, sub_comparisons, sub_movements = heapify(data, n, largest, (0, 0))
        comparisons += sub_comparisons
        movements += sub_movements

    return data, comparisons, movements

def heap_sort(data):
    comparisons, movements = 0, 0
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        data, sub_comparisons, sub_movements = heapify(data, n, i, (0, 0))
        comparisons += sub_comparisons
        movements += sub_movements

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        movements += 2
        data, sub_comparisons, sub_movements = heapify(data, i, 0, (0, 0))
        comparisons += sub_comparisons
        movements += sub_movements

    return data, comparisons, movements

def merge_sort(arr):
    # 비교 횟수와 이동 횟수를 저장할 변수 초기화
    comparisons = 0
    movements = 0
    if len(arr) % 2 == 1:
        comparisons=1

    def merge(left, right):
        # 병합 단계에서 비교와 이동 횟수를 추적하기 위한 변수
        nonlocal comparisons, movements
        result = []  # 병합 결과를 저장할 리스트
        i = j = 0  # 각 배열의 인덱스를 추적

        # 두 배열을 병합하는 과정에서 비교 및 정렬 수행
        while i < len(left) and j < len(right):
            comparisons += 1  # 두 요소를 비교했으므로 비교 횟수 증가
            if left[i] <= right[j]:
                result.append(left[i])  # 왼쪽 배열의 요소를 결과 리스트에 추가
                movements += 1  # 요소 이동 횟수 증가
                i += 1  # 왼쪽 배열의 다음 요소로 이동
            else:
                result.append(right[j])  # 오른쪽 배열의 요소를 결과 리스트에 추가
                movements += 1  # 요소 이동 횟수 증가
                j += 1  # 오른쪽 배열의 다음 요소로 이동

        # 남아 있는 요소들을 결과 리스트에 추가 (비교 없이 이동만 수행)
        result.extend(left[i:])  # 왼쪽 배열의 나머지 요소 추가
        movements += len(left) - i  # 남은 요소 개수만큼 이동 횟수 증가
        result.extend(right[j:])  # 오른쪽 배열의 나머지 요소 추가
        movements += len(right) - j  # 남은 요소 개수만큼 이동 횟수 증가

        return result  # 병합된 결과 반환

    def sort(sub_array):
        # 배열의 길이가 1 이하일 경우 정렬할 필요가 없으므로 그대로 반환
        nonlocal comparisons, movements

        if len(sub_array) <= 1:
            return sub_array

        # 배열을 중간 기준으로 두 부분으로 분할
        mid = len(sub_array) // 2
        left = sort(sub_array[:mid])  # 왼쪽 부분 배열 재귀적으로 정렬
        right = sort(sub_array[mid:])  # 오른쪽 부분 배열 재귀적으로 정렬

        # 병합 단계 수행
        merged_result = merge(left, right)

        return merged_result

    # 병합 정렬 실행
    sorted_data = sort(arr)
    return sorted_data, comparisons, movements


def quick_sort(data):
    def quick_sort_recursive(A, left, right, comparisons, movements):
        if left < right:  # 정렬 범위가 2개 이상일 경우만 실행
            q, comparisons, movements = partition(A, left, right, comparisons, movements)
            comparisons, movements = quick_sort_recursive(A, left, q - 1, comparisons, movements)
            comparisons, movements = quick_sort_recursive(A, q + 1, right, comparisons, movements)
        return comparisons, movements

    def partition(A, left, right, comparisons, movements):
        pivot = A[left]  # 피벗은 리스트의 첫 번째 요소로 설정
        low = left + 1
        high = right

        while True:
            # 피벗보다 작은 값을 찾기 위해 low를 오른쪽으로 이동
            while low <= right and A[low] < pivot:
                low += 1
                comparisons += 1  # 비교 증가
            # 조건 실패로 루프가 종료될 때 추가 비교는 기록하지 않음

            # 피벗보다 큰 값을 찾기 위해 high를 왼쪽으로 이동
            while high >= left and A[high] > pivot:
                high -= 1
                comparisons += 1  # 비교 증가
            # 조건 실패로 루프가 종료될 때 추가 비교는 기록하지 않음

            if low < high:  # low와 high가 교차하지 않은 경우
                A[low], A[high] = A[high], A[low]
                movements += 2
            else:
                break

        A[left], A[high] = A[high], A[left]
        movements += 2
        return high, comparisons, movements

    comparisons, movements = 0, 0
    comparisons, movements = quick_sort_recursive(data, 0, len(data) - 1, comparisons, movements)
    return data, comparisons, movements


def radix_sort(data):
    comparisons, movements = 0, 0  # 비교 횟수와 이동 횟수를 초기화

    def counting_sort(arr, exp):
        nonlocal comparisons, movements  # 외부 변수 comparisons와 movements를 사용
        n = len(arr)  # 배열의 길이를 저장
        output = [0] * n  # 정렬된 데이터를 저장할 배열
        count = [0] * 10  # 각 자릿수(0~9)의 빈도수를 저장할 배열

        # 1단계: 자릿수를 기준으로 빈도수를 계산
        for i in range(n):
            index = (arr[i] // exp) % 10  # 현재 자릿수 값 계산
            count[index] += 1  # 해당 자릿수 값에 대한 빈도수 증가

        # 2단계: count 배열을 누적합으로 변환하여 위치 계산
        for i in range(1, 10):
            count[i] += count[i - 1]  # 이전 값과 현재 값을 누적

        # 3단계: 배열을 뒤에서부터 순회하며 정렬된 위치에 값 저장
        for i in range(n - 1, -1, -1):  # 안정성을 유지하기 위해 역순으로 진행
            index = (arr[i] // exp) % 10  # 현재 자릿수 값 계산
            output[count[index] - 1] = arr[i]  # 정렬된 위치에 값 저장
            count[index] -= 1  # 해당 자릿수의 위치 감소
            movements += 1  # 이동 횟수 증가 (output 배열에 삽입)

        # 4단계: 정렬된 값을 원래 배열로 복사
        for i in range(n):
            arr[i] = output[i]  # output 배열의 값을 원래 배열에 복사
            movements += 1  # 이동 횟수 증가 (원래 배열로 복사)

    # 최대값의 자릿수만큼 반복
    max_val = max(data)  # 배열의 최대값 계산
    exp = 1  # 자릿수를 나타내는 변수 (1의 자리부터 시작)
    while max_val // exp > 0:  # 자릿수만큼 반복 (최대값의 자릿수 계산)
        counting_sort(data, exp)  # 현재 자릿수를 기준으로 정렬
        exp *= 10  # 다음 자릿수로 이동 (1 -> 10 -> 100 등)

    # 정렬된 배열, 비교 횟수, 이동 횟수를 반환
    return data, comparisons, movements

def main():
    sort_algorithms = {
        "SEL": selection_sort,
        "INS": insertion_sort,
        "BUB": bubble_sort,
        "SHE": shell_sort,
        "HEA": heap_sort,
        "MER": merge_sort,
        "QUI": quick_sort,
        "RAD": radix_sort
    }

    data_input = input("* Please input a data list (comma-separated): ")
    data = list(map(int, data_input.split(",")))

    print("\n* Target Sorting Algorithm List")
    print(" Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")

    algo_choice = input("* Select sorting algorithm: ").upper()

    if algo_choice in sort_algorithms:
        sorted_data, comparisons, movements = sort_algorithms[algo_choice](data[:])
        print(f"\n>> Sorted : {', '.join(map(str, sorted_data))}")
        print(f">> Number of Comparisons : {comparisons}")
        print(f">> Number of Data Movements : {movements}")
    else:
        print("Invalid algorithm choice. Please try again.")

if __name__ == "__main__":
    main()


