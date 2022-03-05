# 프로그래머스 | [1차]비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 수도코드 : 2진수, 비트연산자 사용
# bin(n) - n정수 2진수 변환
# .rjust(5, '0') - 문자열 정렬. 왼쪽으로 5만큼 정렬, 빈칸을 '0'으로.
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = str(bin(i|j)[2:]).rjust(n, '0')
        b = a.replace('0',' ')
        answer.append(b.replace('1','#'))
    return answer
# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))