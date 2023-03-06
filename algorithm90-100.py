# 프로그래머스 | 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""
문제이해
s 매개변수 알파벳은 암호 풀이 시작점
skip 매개변수 알파벳은 넘어감
index 매개변수 수만큼 뒤로

사용
아스키코드 chr() - 97부터 123까지 lowerCase

수도코드
alphabet = 알파벳 전체 - skip
s와 index 기준으로 암호 풀이
"""

def solution1(s, skip, index):
    answer = ""
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    for alpha in s:
        answer += alphabet[(alphabet.index(alpha) + index) % len(alphabet)]
    return answer

print(solution1("aukks", "wbqd", 5))


# 프로그래머스 | 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""
문제 이해 
return 유효기간이 지난 정보

수도코드
terms_dict = {약관 종류 : 총일수(오늘날짜-유효기간)}
if 수집일자 <= terms_dict: 출력
"""
def day(today):
    return int(today[0:4])*12*28 + int(today[5:7])*28 + int(today[8:])

def solution2(today, terms, privacies):
    terms_dict = {term[0]: day(today) - int(term[2:])*28 for term in terms}

    answer = []
    for num, privacie in enumerate(privacies):
        if  day(privacie[:10]) <= terms_dict[privacie[-1:]]:
            answer.append(num+1)
    return answer

# print(solution2("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))


def solution3(book_time):
    booking = [(int(start[:2]) * 60 + int(start[3:]), (int(end[:2]) * 60 + int(end[3:]) + 10)) for start, end in book_time]
    booking.sort()
    update = []
    # [(850, 1170), (860, 930), (900, 1030), (1000, 1110), (1100, 1290)]
    
    for start, end in booking:
        if not update:
            update.append(end)
            continue
        if update[0] <= start:
            update[0] = end
        else:
            update.insert(0, end)

        
    return len(update)

print(solution3([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))