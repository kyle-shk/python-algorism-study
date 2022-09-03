"""
 *packageName    : 
 * fileName       : 배달
 * author         : ipeac
 * date           : 2022-09-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-02        ipeac       최초 생성
 """

# road 의 길이 3,
# N : 마을의 개수
# a b : 도로가 연결하는 두 마을의 번호
# c : 도로를 지나는 데 걸리는 시간
# K ; 음식을 배달하는 데 걸리는 시간
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return
import heapq

def dijkstra(dist, adj):
    # 출발노드 기준으로 각 노드들의 최소비용의 탐색
    heap = []
    heapq.heappush(heap, [0, 1])  # 거리, 노드
    while heap:
        cost, node = heapq.heappop(heap)
        
        for c, n, in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [cost + c, n])

def solution(N, road, K):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    adj = [[] for _ in range(N + 1)]  # 인접 노드 & 거리 기록할 배열
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    dijkstra(dist, adj)
    return len([i for i in dist if i <= K])

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
# print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
