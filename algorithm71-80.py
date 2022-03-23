# 백준 | 약수
# https://www.acmicpc.net/problem/1037
# 약수의 최대값 최소값을 곱하면 원래 숫자가 나오는 원리
def baekjoon(num):
    num.sort()
    NumMin = num[0]
    NumMax = num[-1]
    return NumMin * NumMax
# print(baekjoon([3,4,2,12,6,8]))
