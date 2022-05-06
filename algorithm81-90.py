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


# 프로그래머스 | 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935
# divmod(n, 3) : 매개변수로 두개의 숫자를 입력받아 몫과 나머지를 튜플로 반환, 파이썬 내장 함수.
# int(value, base) : base진법 10진법으로 변환
def solution(n):
    answer = "" # 반전 상태로 저장
    while True:
        n, rest = divmod(n, 3)
        answer += str(rest)

        if n == 0:
            break
    
    return int(answer, 3)
# print(solution(45))


# 프로그래머스 | 신규아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
# 정규표현식 사용
import re
def solution(new_id):
    re_id = new_id
    re_id = re_id.lower()
    re_id = re.sub('[^a-z0-9\-_.]', '', re_id)
    re_id = re.sub('\.+', '.', re_id)
    re_id = re.sub('^[.]|[.]$', '', re_id)
    re_id = 'a' if len(re_id) == 0 else re_id[:15]
    re_id = re.sub('^[.]|[.]$', '', re_id)
    re_id = re_id if len(re_id) > 2 else re_id + "".join([re_id[-1] for i in range(3-len(re_id))])
    return re_id
# print(solution("abcdefghijklmn"))


# 프로그래머스 | [1차] 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 스택으로 문제 풀기
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace("10", "A")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for i in dartResult:
        if i.isdigit() or i=='A':
            answer.append(10 if i == 'A' else int(i))
        elif i in ('S', 'D', 'T'):
            num = answer.pop()
            answer.append(num ** bonus[i])
        elif i == '#':
            answer[-1] *= -1
        elif i == '*':
            num = answer.pop()
            if len(answer):
                answer[-1] *= 2
            answer.append(2 * num)
    return sum(answer)
# print(solution("1D#2S*3S"))


# 프로그래머스 | 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# 절대값 abs(값)
# 몫과 나머지 divmod( , )
def solution(numbers: list, hand: str)-> str:
    answer = ""
    L = [1,4,7]
    R = [3,6,9]
    right = 10 # 오른손 위치
    left = 12 #왼손 위치
    for i in numbers:
        if i in L:
            answer+= "L"
            left = i
        elif i in R:
            answer+= "R"
            right = i
        else:
            i = 11 if i == 0 else i # 0자리에는 값 11을 부여한다
            if sum(divmod(abs(i-right), 3)) > sum(divmod(abs(i-left), 3)): # 원소간 절대값을 구해 3으로 나눈 몫과 나머지를 더한 값 비교
                answer+= "L"
                left = i
            elif sum(divmod(abs(i-right), 3)) < sum(divmod(abs(i-left), 3)):
                answer+= "R"
                right = i
            else:
                if hand == "right":
                    answer+= "R"
                    right = i
                else:
                    answer+= "L"
                    left = i
    return answer
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))


# 프로그래머스 | 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
# is_prime_num(n) n 으로 구할 수 있지만, 시간복잡도 줄이기 -> int(math.sqrt(n))+1
# list n조합 구하기 : combinations(list,n)
import math
from itertools import combinations
# 소수 판별
def is_prime_num(n: int)-> bool:
    for i in range(2, int(math.sqrt(n))+1): # 반복 범위 줄이기
        if n % i == 0:
            return False
    return True

def solution(nums: list)-> int:
    answer = 0
    num = list(combinations(nums,3)) # nums배열 원소3개씩 조합한 list 생성
    for i in num:
        if is_prime_num(sum(i)):
            answer += 1             
    return answer
    