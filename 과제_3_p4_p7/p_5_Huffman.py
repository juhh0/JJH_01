class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char  # 문자
        self.freq = freq  # 빈도수
        self.left = None  # 왼쪽 자식
        self.right = None  # 오른쪽 자식

    # 노드 비교를 위해 연산자 오버로딩
    def __lt__(self, other):
        return self.freq < other.freq


def heappush_min(heap, node):
    heap.append(node)          # 맨 마지막 노드로 일단 삽입
    i = len(heap) - 1          # 노드 n의 위치
    while i > 1:               # 루트가 아니면 up-heap 진행
        pi = i // 2            # 부모 노드의 위치
        if heap[pi].freq <= node.freq:  # 부모가 더 작으면 종료
            break
        heap[i] = heap[pi]     # 부모를 아래로 내림
        i = pi
    heap[i] = node             # 마지막 위치에 삽입


def heappop_min(heap):
    size = len(heap) - 1       # 힙 크기
    if size == 0:              # 공백 상태
        return None

    root = heap[1]             # 루트 노드 저장
    last = heap[size]          # 마지막 노드
    pi = 1                     # 부모 인덱스
    i = 2                      # 자식 인덱스

    while i <= size:           # 마지막 노드 이전까지
        if i < size and heap[i].freq > heap[i + 1].freq:  # 오른쪽 자식이 더 작으면
            i += 1
        if last.freq <= heap[i].freq:  # 마지막 노드가 더 작으면 종료
            break
        heap[pi] = heap[i]     # 자식을 위로 올림
        pi = i
        i *= 2

    heap[pi] = last            # 마지막 노드를 삽입
    heap.pop()                 # 마지막 노드 제거
    return root                # 루트 반환


def build_huffman_tree(frequencies):
    heap = [0]  # 최소힙 초기화
    # 문자와 빈도수를 HuffmanNode로 변환하여 힙에 삽입
    for char, freq in frequencies.items():
        heappush_min(heap, HuffmanNode(char, freq))

    # Huffman Tree 생성
    while len(heap) > 2:  # 루트만 남을 때까지 반복
        left = heappop_min(heap)
        right = heappop_min(heap)
        # 병합된 노드 생성
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush_min(heap, merged)

    return heappop_min(heap)  # 최종 루트 노드 반환


def generate_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node:
        if node.char is not None:  # 리프 노드
            codes[node.char] = current_code
        generate_huffman_codes(node.left, current_code + "0", codes)
        generate_huffman_codes(node.right, current_code + "1", codes)
    return codes


def encode(input_string, codes):
    encoded_bits = []
    for char in input_string:
        encoded_bits.append(codes[char])  # 각 문자의 Huffman Code 추가
    return ''.join(encoded_bits)


def calculate_compression_rate(input_string, encoded_string):
    original_size = len(input_string) * 8  # ASCII는 8비트 사용
    compressed_size = len(encoded_string)
    return (1 - compressed_size / original_size) * 100

def main():
    # 코딩 대상 문자 입력
    while True:
        characters = input("코딩대상문자: ").strip()
        if characters:
            break
        print("illegal Character")

    # 빈도수 입력
    print("\n빈도수:")
    frequencies = {}
    for char in characters:
        while True:
            try:
                freq = int(input(f"Frequency of '{char}': "))
                if freq <= 0:
                    print("Frequency must be a positive integer.")
                    continue
                frequencies[char] = freq
                break
            except ValueError:
                print("Please enter a valid integer.")

    # Huffman Tree 생성 및 코드 생성
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Huffman Codes 출력
    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    # 입력된 문자열 인코딩
    encoded_string = encode(characters, huffman_codes)

    # 압축률 계산
    compression_rate = calculate_compression_rate(characters, encoded_string)

    # 결과 출력
    print("\nEncoded Result (비트 열):")
    print(encoded_string)

    print(f"\nCompression Rate: {compression_rate:.2f}%")


if __name__ == "__main__":
    main()