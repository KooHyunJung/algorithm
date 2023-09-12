# 프로그래머스 | 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""
문제이해
s 매개변수 알파벳은 암호 풀이 시작점
skip 매개변수 알파벳은 넘어감
index 매개변수 수만큼 뒤로

사용
아스키코드 chr() - 97부터 123까지 lowerCase

수도코드
alphabet = 알파벳 전체 - skip
s와 index 기준으로 암호 풀이
"""

def solution1(s, skip, index):
    answer = ""
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    for alpha in s:
        answer += alphabet[(alphabet.index(alpha) + index) % len(alphabet)]
    return answer

print(solution1("aukks", "wbqd", 5))


# 프로그래머스 | 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""
문제 이해 
return 유효기간이 지난 정보

수도코드
terms_dict = {약관 종류 : 총일수(오늘날짜-유효기간)}
if 수집일자 <= terms_dict: 출력
"""
def day(today):
    return int(today[0:4])*12*28 + int(today[5:7])*28 + int(today[8:])

def solution2(today, terms, privacies):
    terms_dict = {term[0]: day(today) - int(term[2:])*28 for term in terms}

    answer = []
    for num, privacie in enumerate(privacies):
        if  day(privacie[:10]) <= terms_dict[privacie[-1:]]:
            answer.append(num+1)
    return answer

# print(solution2("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))


# 프로그래머스 | 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
from collections import deque

def solution3(numbers):
    answer = [-1] * len(numbers)
    stack=deque()
    
    for val_index, val in enumerate(numbers):
        while len(stack) and stack[-1][0] < val:
            answer[stack[-1][1]] = val
            stack.pop()
        stack.append((val,val_index))
    
    return answer

print(solution3([2, 3, 3, 5]))


# 프로그래머스 | 혼자서 하는 틱택토
# https://school.programmers.co.kr/learn/courses/30/lessons/160585
"""
수도코드
O, X 에 대한 자리값을 저장
이긴 수 축적하여 마지막 판별해준다
"""
def solution4(board):
    if len(board[0]) > 3 or len(board[1]) > 3 or len(board[2]) > 3:
        return 0
    
    result = {"O": [], "X": []}
    for num_0, line in enumerate(board):
        for num_1, val in enumerate(line):
            if val == "O" or val == "X":
                result[val].append((num_0*3) + (num_1+1))
    
    win_O, win_X = 0, 0
    if len(result["O"]) < 3:
        if len(result["O"]) == len(result["X"]) + 1:
            return 1
        if len(result["O"]) == len(result["X"]):
            return 1
        if len(result["O"]) - len(result["X"]) == 0:
            return 1
    else: # len(result["O"]) >= 3:
        if result["O"][2] - result["O"][1] == result["O"][1] - result["O"][0]:
            win_O += 1
        if result["X"][2] - result["X"][1] == result["X"][1] - result["X"][0]:
            win_X += 1
            
    return 0


print(solution4(["O.X", ".O.", "..X"]))


"""
자료구조 깊이/너비 우선탐색(DFS/BES)
깊이 우선탐색 스택 - list 그 자체
너비 우선탐색 큐 - from collections import deque 사용
"""
def solution5(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution5([4, 1, 2, 1], 4))


# 다른 사람 풀이( 순혈 조합 )
from itertools import product

def solution5(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


"""
자료구조 Heap
"""
import heapq

def solution6(operations):
    heap = []
    for operation in operations:
        val = operation.split()
        if "I" == val[0]:
            heapq.heappush(heap, val[1])
        elif "D" == val[0] and val[1] == "-1":
            if heap:
                heapq.heappop(heap)
        elif "D" == val[0] and val[1] == "1":
            if heap:
                max_val = max(heap)
                heap.remove(max_val)

    if not heap:
        return [0, 0]
    else:
        return max(heap), heap[0]


# print(solution6(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


"""
그리드 알고리즘 Kruskal
노드 - 간선 최소비용
"""
def solution7(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 첫번째 노드 담고 시작, 연결된 노드 담김
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer

print(solution7(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


"""
자료구조 해시(object)
"""
def solution7(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for num, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(num, play)]
        else:
            dic1[genre].append((num, play))

        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

print(solution7(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


"""
스택 / 큐
"""
def solution8(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer


from collections import deque

def solution8(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    truck_bridge_deque = deque(bridge_length * [0])
    truck_weights_deque = deque(truck_weights)
    while len(truck_bridge_deque):
        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()
        if truck_weights_deque:
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)
    return answer


"""
네트워크 깊이/너비 우선탐색(DFS/BES)
"""
def solution9(n, computers):
    result = 0
    node = [0] * n
    
    def dfs(pc):
        node[pc]=1
        for idx,c in enumerate(computers[pc]):
            if c and node[idx]==0:
                dfs(idx)
                
    for pc in range(n):
        if node[pc] == 0:
            dfs(pc)
            result+=1
    return result

# print(solution9(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
