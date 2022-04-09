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
