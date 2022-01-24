# 프로그래머스 | 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = (a+b)*(abs(a-b)+1)/2
    return answer



# 프로그래머스 | 자연수 뒤집어 배열
# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = list(map(int,list(str(n)[::-1])))
    return answer



# 프로그래머스 | 가운데 수 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s))/2-1:(len(s))/2+1]
    else:
        return s[(len(s))//2]


# 프로그래머스 |핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python
def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]


# 프로그래머스 | 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):         # 1은 무조건 나머지가 0. 따라서 2부터 시작. 2~(n-1)까지.
    for i in range(2,n): # 하지만 1부터 시작해도 문제는 없음.
        if n % i == 1:   # 가장 먼저 나머지가 1이 되는 숫자를
            return i