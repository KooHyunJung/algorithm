# 프로그래머스 | 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    a = list(map(int, str(n)))
    a.sort(reverse=True)
    return int("".join(map(str, a)))

# print(solution(118372))


# 프로그래머스 | 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 수도코드
# 원소가 0 이상 1,000 이하이기로 매개변수 원소에 3곱하기 -> ['300300300300', '30303030', '3333']
# numbers와 num1 하나로 묶어주기(2차원 리스트)
# num1 기준으로 오름차순 정렬 ->[('3333', 3), ('30303030', 30), ('300300300300', 300)]
# numbers만 answer = '' 더하기
# 마지막에 [0,0,0] -> "000" 방지를 위해 int로 묶고 str로 출력.
def solution(numbers):
    num1 = []
    answer = ''
    for i in numbers:
        num1.append(str(i)*3)
    Numlist = list(zip(num1,numbers))
    Numlist.sort(reverse=True)
    for i in range(len(Numlist)):
        answer+=str(Numlist[i][1])
    return str(int(answer))

#print(solution([300, 30, 3]))