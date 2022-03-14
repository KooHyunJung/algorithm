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
