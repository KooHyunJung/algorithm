# 프로그래머스 | 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i ==0:
            answer.append(i)
    return sum(answer)


# 프로그래머스 | 두 개 뽑아 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

# 경우의 수를 생각한다. 하지만 중복은 제외하고 오름차순으로 리턴해야 한다.
def solution(num):
    answer = []
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if (num[i] + num[j]) not in answer:
                answer.append(num[i] + num[j])
    answer.sort()      
    return answer

# a = [5,0,2,7]
# print(solution(a))


# 프로그래머스 | 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

# 슈도코드
# 단어(공백을 기준)별로 짝/홀수 인덱스
# 인덱스가 짝수인지 홀수인지 판별 (0번째는 짝수)
# 문자열 길이로 for문 돌려 자리값으로 i,j가 돌아가게 한다
# 각 조건문 아래서 값을 추출해서 처리
# .split(구분자) 함수에 문자열을 넣으면 한 문자씩 다 나누어 리스트를 생성
# .lower()
# .upper()
# '구분자'.join(리스트)
def solution(s): 
    answer = []
    for ws in s.split(" "):
        a =""
        for i in range(len(ws)):
            if i % 2 ==0:
                a += ws[i].upper()
            else:
                a += ws[i].lower()
        answer.append(a)
    return " ".join(answer)

# a = "t tt t ttt"
# print(solution(a))