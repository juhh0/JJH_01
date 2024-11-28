# 최소 힙을 구성하기 위한 heappush, heappop 함수
def heappush(heap, node):
    heap.append(node)      # 힙의 마지막에 노드를 추가
    i = len(heap) - 1      # 새로운 노드의 인덱스
    while i > 1:
        pi = i // 2        # 부모 노드의 인덱스
        if heap[pi].freq <= node.freq:
            break
        heap[i] = heap[pi]  # 부모 노드를 아래로 이동
        i = pi
    heap[i] = node          # 새로운 위치에 노드 삽입

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]          # 루트 노드를 꺼냄
    last = heap[size]       # 마지막 노드를 가져옴
    pi = 1                  # 부모 노드의 인덱스
    i = 2                   # 자식 노드의 인덱스

    while i <= size:
        if i < size and heap[i].freq > heap[i + 1].freq:
            i += 1          # 오른쪽 자식이 더 작으면 오른쪽으로 이동
        if last.freq <= heap[i].freq:
            break
        heap[pi] = heap[i]  # 자식 노드를 위로 이동
        pi = i
        i *= 2

    heap[pi] = last          # 마지막 노드를 최종 위치에 삽입
    heap.pop()               # 힙 크기 감소
    return root              # 루트 노드를 반환

# Huffman 트리를 구성하기 위한 노드 클래스
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

# Huffman 트리를 구성하는 함수
def build_huffman_tree(chars, freqs):
    heap = [None]  # 최소 힙을 사용하기 위해 첫 요소를 None으로 설정
    for i in range(len(chars)):
        heappush(heap, Node(freqs[i], chars[i]))

    while len(heap) > 2:
        left = heappop(heap)
        right = heappop(heap)
        merged = Node(left.freq + right.freq, None, left, right)
        heappush(heap, merged)

    return heappop(heap)

# Huffman 코드를 생성하는 함수
def generate_codes(root):
    huffman_codes = {}

    def _generate_code(node, current_code):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            _generate_code(node.left, current_code + '0')
            _generate_code(node.right, current_code + '1')

    _generate_code(root, "")
    return huffman_codes

# 입력된 텍스트를 Huffman 코드로 인코딩하는 함수
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# 압축률을 계산하는 함수
def calculate_compression_rate(orig_text, encoded_text):
    orig_size = len(orig_text) * 8  # ASCII 기준
    comp_size = len(encoded_text)
    comp_rate = (1 - comp_size / orig_size) * 100
    return comp_rate

# Huffman Coding 프로그램
def huffman_coding_program():
    # 문자와 빈도수
    chars = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]

    # Huffman Tree 생성
    root = build_huffman_tree(chars, freqs)
    huffman_codes = generate_codes(root)

    # 입력 받기 및 유효성 검사
    while True:
        text = input("Please a word: ").strip()
        if not all(c in chars for c in text):
            print("illegal character")
        else:
            break

    # 인코딩 및 출력
    encoded_text = encode_text(text, huffman_codes)
    compression_rate = calculate_compression_rate(text, encoded_text)
    print("결과 비트 열:", encoded_text)
    print("압축률: {:.2f}%".format(compression_rate))

# 프로그램 실행
if __name__ == "__main__":
    huffman_coding_program()
