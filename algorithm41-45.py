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


# 프로그래머스 | 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = []
    for i in range(10):
        if i not in numbers:
            answer.append(i)
    return sum(answer)
# 다른 풀이   
# def solution(numbers):
#     return 45 - sum(numbers)
# print(solution([1,2,3,4,6,7,8,0]))


# 프로그래머스 | 문자열 내 마음대로 정하기
# https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    a = []
    for i in strings:
        a.append(i[n]+i)
    answer = dict(zip(strings,a))
    return list(dict(sorted(answer.items(), key=lambda x: x[1])).keys())
#print(solution(["abce", "abcd", "cdx"], 2))


# 프로그래머스 | 하샤드 수 
# https://programmers.co.kr/learn/courses/30/lessons/12947
# int를 str로 변경
def solution(x):
    answer = 0
    for i in range(len(str(x))):
        answer += int(str(x)[i])
    return True if x % answer == 0 else False
#print(solution(13))


# 프로그래머스 | 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884
# 수도코드
# 제곱수 약수의 개수는 항상 홀수이다. 따라서 num이 제곱수인지 판별.
# math.sqrt() 제곱근을 반환하는 함수.
# .is_integer() 5.0 정수 판별.
import math
def solution(left : int, right: int) -> int:
    answer = 0
    for num in range(left,right+1):
        if math.sqrt(num).is_integer():
            answer -= num
        else: answer += num
    return answer
# print(solution(24,27))