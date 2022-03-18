# 백준 | 알람시계
# https://www.acmicpc.net/problem/2884
a, b = 0, 30
if a >= 1:
    print(((a*60 + b) -45) // 60, ((a*60 + b) -45) % 60)
else:
    print(23, ((a*60 + b) -45) % 60)


# 백준 | 더하기 사이클
# https://www.acmicpc.net/problem/1110
a = 26
count = 0
num = a

while True:
  num1 = num // 10
  num2 = num % 10
  num3 = (num1 + num2) % 10
  num = (num2 * 10) + num3
  count += 1
  if num == a:
    break
print(count)


# 백준 | 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
a = [5, 50, 50, 70, 80, 100]
nums = []
average = sum(a[1:])/a[0]
for i in a[1:]:
    if i > average:
        nums.append(i)
answer = len(nums)/a[0] *100
print(f'{answer:.3f}%')


# 백준 | 셀프넘버
# https://www.acmicpc.net/problem/4344
num1 = set(range(1, 10001)) # 1~1000까지
num2 = set()   # [생성자] 담을 곳, 중복 방지 set
# [생성자]를 먼저 찾아 준다
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num2.add(i)
# num1 - num2 : 셀프넘버 구하기
self_num = sorted(num1 - num2)
for i in self_num:
    print(i)
