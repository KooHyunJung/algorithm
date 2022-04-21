# 백준 | 균형잡힌 세상 | stack
# https://www.acmicpc.net/problem/4949
# 함수로 변형
def stack1(string: str)-> str:
    stack = []
    true_flag = 1

    for cha in string:
        if cha == '(' or cha == '[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break

    if string == '.':
        pass
    return "yes" if true_flag and not stack else "no"
# print(stack1("A rope may form )( a trail in a maze."))


# 백준 | 회전하는 큐
# https://www.acmicpc.net/problem/1021
# deque(데크) 양방향 큐:
# 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도 제공.
# .popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
# .rotate(num): 데크를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)
from collections import deque
def deque1(n: int, index: list)-> int:
    data = deque([i for i in range(1,n+1)]) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    count = 0

    for num in index:
        while 1:
            if data[0] == num:
                data.popleft()
                break
            else:
                if data.index(num) <= len(data)//2:
                    data.rotate(-1)
                    count += 1
                else:
                    data.rotate(1)
                    count += 1
    return count
# print(deque1(10,[2,9,5]))


# 백준 | 통계학
# https://www.acmicpc.net/problem/2108
# 함수로 변형해서 풀이
# round() : 파이썬 반올림 함수
# Counter(N).most_common() -> .most_common() : N의 요소 중 개수가 많은 순으로 정렬된 배열 리턴
from collections import Counter
def baekjoon(N: list)->list:
    N.sort()
    # 산술평균
    arithmetic_mean = round(sum(N)/len(N))
    # 중앙값
    median = N[int((len(N)-1)/2)]
    # 최빈값
    mode = 0
    count = Counter(N).most_common() # .most_common(3) 개수 지정도 가능
    if len(count) > 1:
        if count[0][1] == count[1][1]:
            mode += count[1][0]
        else:
            mode += count[0][0]
    else:
        mode + count[0][0]
    # 범위
    range = N[-1] - N[0]

    result = [arithmetic_mean, median, mode, range]
    return result
# print(baekjoon([1,3,8,-2,2]))


# 백준 | 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 분할 정복 : 그대로 해결할 수 없는 문제를 작은 문제로 분할하여 문제를 해결하는 방법으로
# 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄어가는 방식이다.
import sys

N = int(sys.stdin.readline())
piece = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def division(x, y, n):
    global blue, white
    check = piece[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != piece[i][j]:
                division(x,y,n//2) # 1
                division(x,y+n//2,n//2) # 2
                division(x+n//2,y,n//2) # 3
                division(x+n//2,y+n//2,n//2) # 4
                return
    if check==0:
        white+=1
        return
    else:  
        blue+=1
        return
            
division(0,0,N)
print(white)
print(blue)

