# 프로그래머스 | 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926
# 수도코드
# 아스키코드 활용
def solution(s:str, n:int)->str:
    answer = ''
    for i in range(len(s)):
        if 64 < ord(s[i]) < 91:
            answer += chr((ord(s[i])-65+n)%26 + 65)
        elif 96 < ord(s[i]) < 123:
            answer += chr((ord(s[i])-97+n)%26 + 97)
        else: answer += s[i]
    return answer
# print(solution("a B z", 4))


# 프로그래머스 | 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969
a, b = map(int, input().strip().split(' '))
for i in range(1,b+1):
    print((i+(a-i)) * '*')


# 프로그래머스 | 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934
# math.sqrt() 제곱근을 반환하는 함수.
# math.pow(n, m) n의 m승을 반환하는 함수. 
import math
def solution(n):
    if math.sqrt(n).is_integer():
        NewNum = math.sqrt(n) + 1
        return int(math.pow(NewNum, 2))
    else: return -1
# print(solution(3))
# print(solution(121))


# 프로그래머스 | 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution1(s):
    NewStr = s
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, alpanum in enumerate(num):
        NewStr=NewStr.replace(alpanum,str(index))
    return int(NewStr)
# print(solution1("oneseven8eight"))
