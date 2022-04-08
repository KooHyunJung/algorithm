# 백준 | 균형잡힌 세상 | stack
# https://www.acmicpc.net/problem/4949
# 함수로 변형
def stack1(string: str)-> str:
    stack = []
    true_flag = 1

    for cha in string:
        if cha == '(' or cha == '[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break

    if string == '.':
        pass
    return "yes" if true_flag and not stack else "no"
# print(stack1("A rope may form )( a trail in a maze."))
