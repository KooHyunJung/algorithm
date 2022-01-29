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