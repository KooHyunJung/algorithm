# 프로그래머스 | 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 수도코드
# N을 기준으로 stages 요소들을 비교 분석한다
def solution(N, stages):
    # 각 stage 마다 멈춰있는 user 묶어
    answer = [] # [[2, 1, 2, 6, 2, 4, 3, 3], [2, 2, 6, 2, 4, 3, 3], [6, 4, 3, 3], [6, 4], [6]]
    for i in range(1,N+1):
        a = []
        for j in stages:
            if i in range(1,j+1):
                a.append(j)
        answer.append(a)
    # {'stage' : 실패율} 구하기
    b = {} # {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
    for i in range(N):
        if len(answer[i]) !=0:
            c = answer[i].count(i+1) / len(answer[i])
            b[i+1]=c
        else: 
            b[i+1]=0
    # 딕셔너리 '값'을 기준으로 내림차순정렬을 해주고, 키값만 출력!
    d = sorted(b, key=lambda x: b[x], reverse=True) 
    return d # [3,4,2,1,5]

# 몇몇 테스트에서 [시간 초과] 
# 위 스텝 1, 2를 하나로 묶어 코 작성
def solution2(N, stages):
    answer = {} # {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
    StageUser = len(stages)
    for i in range(1,N+1): # 1 2 3 4 5
        if StageUser !=0:
            a = stages.count(i) # 1 3 2 1 0
            answer[i] = a / StageUser
            StageUser -= a # 8 7 4 2 1 1
        else:
            answer[i]= 0
    b = sorted(answer, key=lambda x: answer[x], reverse=True) 
    return b

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# # [3,4,2,1,5]
# print(solution2(N, stages))


# 프로그래머스 | H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747
# 수도코드
# 위키백가, H-index = 계산 방법 오름차순 내림차순으로 비교해서 겹치는 숫자 return
def solution3(citations):
    answer = 0 
    citations.sort(reverse=True) # 내림차순 정렬 [6, 5, 3, 1, 0]
    for i in range(1,len(citations)+1): #오름차순1  2  3  4  5
        if i <= citations[i-1]: 
            answer = i
    return answer

# citations = [3, 0, 6, 1, 5]
# print(solution3(citations))