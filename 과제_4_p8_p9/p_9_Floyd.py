INF = 9999

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end="")
            else:
                print("%4d " % A[i][j], end="")
        print("")


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수

    # 초기 가중치 배열 복사
    A = list(adj)
    for i in range(vsize):
        A[i] = list(adj[i])

    # 경로 추적을 위한 배열 초기화
    path = [[-1 if adj[i][j] == INF or i == j else i for j in range(vsize)] for i in range(vsize)]

    # Floyd 알고리즘 실행
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[k][j]  # 경로 갱신
        printA(A)  # 진행 상황 출력용 (선택적)

    return A, path


def reconstruct_path(start, end, path, vertex):
    """시작 정점에서 종료 정점까지의 최단 경로를 추적"""
    route = []
    if path[start][end] == -1:  # 경로가 없는 경우
        return route

    while end != start:
        route.append(end)
        end = path[start][end]
    route.append(start)
    route.reverse()
    return [vertex[v] for v in route]


if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0],
    ]

    print("Shortest Path By Floyd's Algorithm")

    # Floyd 알고리즘 실행
    dist, path = shortest_path_floyd(vertex, weight)

    # 사용자 입력 처리
    start_vertex = input("\nStart Vertex: ").strip()
    end_vertex = input("End Vertex: ").strip()

    if start_vertex not in vertex or end_vertex not in vertex:
        print("Invalid vertex entered.")
    else:
        start_idx = vertex.index(start_vertex)
        end_idx = vertex.index(end_vertex)

        # 최단 경로와 거리 출력
        shortest_distance = dist[start_idx][end_idx]
        if shortest_distance == INF:
            print(f"* No path exists between {start_vertex} and {end_vertex}.")
        else:
            shortest_path = reconstruct_path(start_idx, end_idx, path, vertex)
            print(f"* Shortest Path: {' -> '.join(shortest_path)}")
            print(f"* Distance of the Shortest Path: {shortest_distance}")
