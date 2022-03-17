# 백준 | 알람시계
# https://www.acmicpc.net/problem/2884
a, b = 0, 30
if a >= 1:
    print(((a*60 + b) -45) // 60, ((a*60 + b) -45) % 60)
else:
    print(23, ((a*60 + b) -45) % 60)
