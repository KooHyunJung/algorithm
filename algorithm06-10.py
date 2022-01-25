# 프로그래머스 | 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    # 찐 체육복 없음. 중복 삭제
    re_lost = set(lost) - set(reserve)
    # 찐 여벌. (여벌도 도난 가능)중복 삭제
    re_reserve = set(reserve) - set(lost)

    # 찐 여벌(re_reserve)로 반복문을 돌린다
    for i in re_reserve:
        if i-1 in re_lost: # 앞번호 학생에게 빌릴 수있는가?
            re_lost.remove(i-1)
        elif i+1 in re_lost: # 뒷번호 학생에게 빌릴 수 있는가?
            re_lost.remove(i+1) # 뒷번호/앞번호 둘 다 못 빌리면 re_lost에 값이 남는다.
    return n - len(re_lost)

# a=20
# b=[1,2,4,20]
# c=[1,3,5,19,20]
# print(solution(a,b,c))


# 프로그래머스 | 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = [] 
    arr.sort() #오름차순으로 바꿔준다
    for i in arr: # arr 요소 하나씩 아래 if 문에 비교해서 나머지가 0인 것은 answer에 저장.
        if i % divisor ==0:
            answer.append(i)
    if not answer: #빈 리스트 확인 방법
        answer = [-1]
    return answer

# a=[3,2,6]
# b=10
# print(solution(a,b))


# 프로그래머스 | 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []    
    for i in range(len(arr)): #배열 길이만큼 값을 비교해 준다.
        if i == 0:            #첫번째 요소는 픽스!
            answer.append(int(arr[i]))
        elif arr[i] != arr[i-1]:   #베열 요소 자리 기준으로 뒤의 자리와 비교해 준다
            answer.append(int(arr[i]))
    return answer

def solution(s):
    a = []
    for i in s:
        print("첫번째",i)
        if a[-1:] == [i]: continue
        a.append(i)
        print("두번쨰",a)
    return a

# a = [1,1,1,3,3,1]
# print(no_continuous(a))
# print(solution(a))


