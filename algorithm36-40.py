# 프로그래머스 | 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    a = list(map(int, str(n)))
    a.sort(reverse=True)
    return int("".join(map(str, a)))

# print(solution(118372))