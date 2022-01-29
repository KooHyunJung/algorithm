# 프로그래머스 | 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            continue
        elif signs[i] == False:
            absolutes[i] = absolutes[i] * -1
    print(absolutes) # [4, -7, 12]
    return sum(absolutes) # 9

absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))



# 구름 | 약수 구하기
# 양의 정수를 입력 받고 그 수의 약수를 모두 출력하시오.
a = 20
for i in range(1,a+1):
    if a % i ==0:
        print(i, end=" ")


# 프로그래머스 | 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 에레토네스의 체
def solution(n):
    a = [False,False] + [True]*(n-1)
    answer=[]

    for i in range(2,n+1):
        if a[i]:
            answer.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return len(answer)


# 프로그래머스 | 행렬에 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950
# 수도코드
# 행, 열 index 기준으로 두 배열의 값을 + 해준다
# 행 = len(arr1)
# 열 = len(arr1[i])
def solution(arr1, arr2):
    b = []
    for i in range(len(arr1)): # 2 / 0, 1 -> 행/세로 크기
        a = []
        for j in range(len(arr1[i])): # 1 / 0 -> 열/가로 크기
            a.append(arr1[i][j] + arr2[i][j])
        b.append(a) 
        print('a',a) #[4]/ [6]
    return b #[[4], [6]]

a1 = [[1],[2]]
a2 = [[3],[4]]
print(solution(a1, a2))


# 프로그래머스 | 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
# 수도코드 
# type(s) = str 형태 변환
# 요소 길이 기준 오름차순 정렬 / sort = 원본을 건드린다, sorted 원본은 냅두고 새로운걸로 만들어서 정렬후 반환
# 요소 비교
def solution(s):
    a = s[2:-2] # 4,2,3},{3},{2,3,4,1},{2,3
    a = a.split('},{') # ['4,2,3', '3', '2,3,4,1', '2,3']
    a = sorted(a, key = len) # ['3', '2,3', '4,2,3', '2,3,4,1']
    
    answer = []
    for a in a:
        a = a.split(',') 
        for a in a:
            if int(a) not in answer:
                answer.append(int(a))
    return answer

# a = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# print(solution(a))