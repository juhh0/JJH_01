from p_7_BinaryTree import *
from p_6_BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent)
    else :
        print("중복된 키 에러")

# AVL 트리의 삭제 연산
def delete_avl(parent, key):
    if parent is None:
        return None

    # 삭제할 노드를 찾기 위한 탐색
    if key < parent.key:
        parent.left = delete_avl(parent.left, key)
    elif key > parent.key:
        parent.right = delete_avl(parent.right, key)
    else:
        # 삭제할 노드를 찾은 경우
        if parent.left is None:  # 왼쪽 자식이 없으면 오른쪽 자식을 반환
            return parent.right
        elif parent.right is None:  # 오른쪽 자식이 없으면 왼쪽 자식을 반환
            return parent.left
        else:
            # 왼쪽과 오른쪽 자식이 모두 있는 경우
            # 오른쪽 서브트리에서 가장 작은 노드를 찾음
            successor = parent.right
            while successor.left is not None:
                successor = successor.left
            # 후계자의 키와 값을 복사
            parent.key = successor.key
            parent.value = successor.value
            # 후계자를 삭제
            parent.right = delete_avl(parent.right, successor.key)

    # 삭제 후 재균형 처리
    return reBalance(parent)


from p_4_CircularQueue import *

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]

    root = None
    # AVL 트리 생성
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)

        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    # AVL 트리에서 노드 삭제
    print("\n[노드 삭제]")
    for key in [9, 6, 2]:
        print(f"삭제({key}): ", end='')
        root = delete_avl(root, key)
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))