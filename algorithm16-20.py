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


# 구름문제 | 문자열 공백 없애기
# replace는 문자열을 변경하는 함수. 문자열 안에서 특정 문자를 새로운 문자로 변경하는 기능을 가지고 있다. 
# 사용 방법은 '변수. replace(old, new, [count])' 형식으로 사용한다.
# - old : 현재 문자열에서 변경하고 싶은 문자
# - new: 새로 바꿀 문자
# - count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 

def Goorm(a):
    return a.replace(" ", "")

b = "  I am Goorm !   "
print(Goorm(b))


# 백준문제 | 크로아티아어
# 수도코드
# 입력값은 소문자와 크로아티아어묶음?으로 이루어져 있음.
# 입력값과 크로아티아어 목록값 비교
# 입력값에 있는 크로아티아어는 "a"로 변경
# 문자열 길이 출력
def baekjoon(b):
    lang = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    for lang in lang:
        b = b.replace(lang, 'a')
    return len(b)

b = "ljes=njak"
print(baekjoon(b))