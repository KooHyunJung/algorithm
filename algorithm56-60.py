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
