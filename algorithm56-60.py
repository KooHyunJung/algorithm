# 프로그래머스 | 크레인 인형뽑기 
# https://programmers.co.kr/learn/courses/30/lessons/64061
# 이렇게 반복문과 조건문을 중첩시켜도 되나 싶다...
def solution(board: list, moves: list) -> int:
    answer = 0
    a = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] !=0:
                a.append(board[j][i-1])
                board[j][i-1] = 0
                if len(a) > 1:
                    if a[-1] == a[-2]:
                        a.pop(-1)
                        a.pop(-1)
                        answer += 2
                break
    return answer
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


# 프로그래머스 | 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
# 왜 아래는 안되는 걸까?
def solution(phone_book):
    SortedPhone = sorted(phone_book, key= len)
    answer = True
    for i in SortedPhone[1:]:
        if SortedPhone[0] == i[:len(SortedPhone[0])]:
            answer = False 
            break
    return answer
# 해쉬 정석 !
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
# print(solution(["12","123","1235","567","88"]))


# 프로그래머스 | 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    # value, index 튜플로 묶어 리스트로 만들어준다
    d = [(v,i) for i,v in enumerate(priorities)]
    answer = 0

    while len(d): # location까지 앞에서부터 비교
      items = d.pop(0)
      if d and max(d)[0] > items[0]:
          d.append(items)
      else:
          answer += 1
          if items[1] == location:
              break
    return answer
# print(solution([1, 1, 9, 1, 1], 1))


# 백준 | 사칙연산
# https://www.acmicpc.net/problem/10869
a, b = 7, 3
answer = [a + b, abs(a - b), a * b, a // b, a % b]
for i in answer:
    print(i)


# 백준 | 곱셈
# https://www.acmicpc.net/problem/2588
a, b = 472, 385
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)
