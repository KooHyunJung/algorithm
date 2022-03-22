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


# 백준 | 단어 공부 
# https://www.acmicpc.net/problem/1157
# collections.Counter(list) 리스트 내 요소 개수 Counter 딕셔너리 형태로 반한
import collections
def baek(a):
    alpha = dict(collections.Counter(list(a.upper())))
    alpha2 = sorted(alpha.items(), key=lambda x:x[1], reverse=True)
    realpha = ""
    num = 0
    for keyy, vall in alpha2:
        if num == 0:
            num += vall
            realpha += keyy
        elif num == vall:
            return "?"
        else:
            return realpha
# print(baek("Mississipi"))


# 백준 | 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]: # 앞 뒤로 같으면 pass
            pass
        elif word[j] in word[j+1:]: # 앞 뒤가 같지 않고, 지금 위치 뒤로 같은 요소가 있으면 -1
            result-=1
            break
print(result)


# 백준 | 설탕 배달
# https://www.acmicpc.net/problem/2839
def baekjoon(sugar):
    count = 0
    while True :
        if sugar % 5 == 0 :
            count += sugar // 5
            return count  
        sugar -= 3
        count += 1 
        
        if sugar <= 0 :
            return -1
# print(baekjoon(4))


# 백준 | Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)
