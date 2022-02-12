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


# 프로그래머스 | 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334
# 수도코드 
# [나쁜유저]가 신고당한 횟수를 구한다
# if [신고당한 횟수] == k(정지 기준): key값을 반환
# [신고한 유저]가 받을 메일과 매칭 시켜준다
def solution(id_list, report, k):
    # [나쁜유저]가 신고당한 횟수를 구한다
    re_report = set(report)
    caution = {} #{'frodo': 2, 'neo': 2, 'muzi': 1}
    for i in re_report:
        a,b=i.split(" ") 
        if caution is None:
            caution[b]=1
        elif b not in caution:
            caution[b]=1
        else: caution[b]+=1
    # [신고당한 횟수] == k: key값 반환
    num = [] #['frodo', 'neo']
    for key,value in caution.items():
        if value >= k:
            num.append(key)
    # [신고한 유저], num(나쁜유저) 매치시켜주기
    userlist = [0] * len(id_list)
    userdict = dict(zip(id_list, userlist)) #{'muzi': 2, 'frodo': 1, 'apeach': 1, 'neo': 0}
    for i in re_report:
        a, b = i.split(" ")
        if b in num:
            userdict[a] += 1
    return list(userdict.values())

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# print(solution(id_list, report, k))


# 프로그래머스 | 부족한 예산 찾기
# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price * i
    answer -= money
    if answer < 0:
        answer = 0
    return answer

# print(solution(3,20,4))


# 프로그래머스 | 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576
# count가 메모리를 많이 쓴다
# 효율성 테스트 실패 [시간초과]
def sol(participant, completion):
    answer = ''
    for i in participant:
        if participant.count(i) > completion.count(i):
            answer += i
            participant.remove(i)
    return answer

# 한 개의 리스트를 {요소:요소개수} 형태로 반환하는 collections 모듈 사용
import collections
def solution(participant, completion):
    a = collections.Counter(participant) - collections.Counter(completion)
    return list(a.keys())[0]

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


# 프로그래머스 | 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    a = seoul.index('Kim')
    return f'김서방은 {a}에 있다'
# 이렇게 작성하는 방법도 았다 > "김서방은 {}에 있다".format(seoul.index('Kim'))
# print(solution(["Jane", "Kim"]))