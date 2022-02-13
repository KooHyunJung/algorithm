# 프로그래머스 | 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
# 수도코드 
# 최대한 많은 부서 지원을 위해, d 오름차순 정렬.
# 반복문을 돌려 budget와 비교.
def solution(d, budget):
    d.sort()
    answer = 0
    count = 0
    for j in d:
        answer += j
        if answer <= budget:
            count += 1
    return count
#print(solution([2,2,3,3], 10))
