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