# 프로그래머스 | 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    if num % 2 == 0:
        return "Even"
    else: 
        return "Odd"

# print(solution(2))


# 프로그래머스 | k번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for val in commands:
        a = array[val[0]-1:val[1]]
        a.sort()
        answer.append(a[val[2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


# 프로그래머스 | 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925
# 아니 이게 뭐람..?
def solution(s):
    return int(s)


# 프로그래머스 | 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if (4 == len(s) or len(s) == 6) and s.isdigit():
        return True
    else:
        return False


# 구름 | 약수 구하기
# 양의 정수를 입력 받고 그 수의 약수를 모두 출력하시오.
a = 20
for i in range(1,a+1):
    if a % i ==0:
        print(i, end=" ")