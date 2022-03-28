# 백준 | 약수
# https://www.acmicpc.net/problem/1037
# 약수의 최대값 최소값을 곱하면 원래 숫자가 나오는 원리
def baekjoon(num):
    num.sort()
    NumMin = num[0]
    NumMax = num[-1]
    return NumMin * NumMax
# print(baekjoon([3,4,2,12,6,8]))


# 백준 | 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
# 최대공약수 math.gcd(a, b)
# 최소공배수 math.lcm(a, b)
import math
def baekjoon(num):
    greatestCD = math.gcd(num[0], num[1])
    LeastCM = math.lcm(num[0], num[1])
    return [greatestCD, LeastCM]
# print(baekjoon([24, 18]))


# 백준 | ACM 호텔
# https://www.acmicpc.net/problem/10250
def baekjoon(array):
    H, _, N = array
    if not N % H:
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H + 1
    return floor*100+num
# print(baekjoon([6, 12, 10]))


# 백준 | 소수구하기
# https://www.acmicpc.net/problem/1929
# 다른거는 함수로 풀다가 이거는 그냥.. 그대로..
# 에라토스테네스의 체
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
 
M, N = map(int, input().split())
for i in range(M, N + 1):
    if isPrime(i):
        print(i)



# 백준 | 나무 자르기
# https://www.acmicpc.net/problem/2805
# 이분탐색(binary search)
def baekjoon_tree(a, tree):
    N, M = a
    tree.sort()

    h = 0
    start =0
    end = tree[-1]
    while start<=end:
        s = 0
        middle = (start + end) // 2
        s = sum(i-middle if i > middle else 0 for i in tree)

        if s >= M:
            h = middle
            start = middle + 1
        else:
            end = middle - 1
    return h
# print(baekjoon_tree([4, 7], [20, 15, 10, 17]))



# 백준 | 스택
# https://hwiyong.tistory.com/185
# 적응 안되는 input으로 알고리즘 문제 풀기..
import sys

def push(x):
    stack.append(x)
def pop():
    return -1 if(not stack) else stack.pop()
def size():
    return len(stack)
def empty():
    return 0 if stack else 1
def top():
    return stack[-1] if stack else -1

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())


# 백준 | 제로
# https://www.acmicpc.net/problem/10773
# 프로그래머스처럼 함수로 풀기
def baekjoon(a):
    answer = []
    for i in a:
        if i == 0:
            answer.remove(answer[-1])
        else:
            answer.append(i)
    return sum(answer)
# print(baekjoon([1,3,5,4,0,0,7,0,0,6]))


# 백준 | 괄호
# https://www.acmicpc.net/problem/9012
# 프로그래머스처럼 함수로 풀기
def baekjoon(a):
    answer = 0
    replace_a = a.replace("()","")
    if replace_a[-1] == "(":
        return "NO"
    for one_a in replace_a:
        if one_a == ")":
            answer += 1
        elif one_a == "(":
            answer -= 1
    
    return "YES" if answer==0 else "NO"
# print(baekjoon("()()()()(()()())()"))
