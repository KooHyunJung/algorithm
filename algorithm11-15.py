# 프로그래머스 | x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    return [ x for x in range(x,(x*n)+1,x)]

def solution(x, n):
    if x >= 0:
        answer = [ x for x in range(x,(x*n)+1,x)]
    else:
        answer = [ x for x in range(x,(x*n)-1,x)]
    return answer

def solution(x, n):
    return [ i * x + x for i in range(n)]

# print(solution(-4,2))


# 프로그래머스 | 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    if len(arr) > 1 :
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

def solution(arr):
    return [i for i in arr if i > min(arr)]
   
# a = [4,3,2,1]
# print(solution(a))


# 프로그래머스 | 2016
# https://programmers.co.kr/learn/courses/30/lessons/12901

# 2016년 1월1일 금요일이다.
# 매월 마지막은 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
def solution(a, b):
    # 금요일부터 시작
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    all_day = day * 53 #366일에 가깝게 요일 리스트를 길게 길게 늘리고 
    last_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print(sum(last_day[:0])+20)
    return all_day[sum(last_day[:a-1])+b-1]

# print(solution(1, 20))