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