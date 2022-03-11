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


# 프로그래머스 | 포켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
    

# 프로그래머스 | 최대공약수와 최소공배수 
# https://programmers.co.kr/learn/courses/30/lessons/12940
# math.gcd(a, b, c, ...) 최대공배수 구하는 매소드
# 또는 [유클리드 호제법] 사용하기
from math import gcd
def solution(n, m):
    num1 = gcd(n, m)
    num2 = n*m // gcd(n,m)
    return [num1, num2]
# print(solution(3, 12))


# 프로그래머스 | 최소직사각형 
# https://programmers.co.kr/learn/courses/30/lessons/86491
# 수도코드: 각 변의 작은값 -> h, 큰값 -> w 
def solution(sizes):
    w = []
    h = []
    for i in sizes:
        if i[0] > i[1]:
            w.append(i[0])
            h.append(i[1])
        else: 
            w.append(i[1])
            h.append(i[0])
    return sorted(w, reverse=True)[0] * sorted(h, reverse=True)[0]
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

