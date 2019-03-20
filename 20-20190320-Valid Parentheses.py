def validParentheses(string):
    stack=[]

    for s in string:
        if s in "{[(":
            stack.append(s)
        else:
            if not stack:return False
            elif s=="}" and stack.pop()!="{":
                return False
            elif s=="]" and stack.pop()!="[":
                return False
            elif s==")" and stack.pop()!="(":
                return False
    if stack==[]:
        return True

s="())"
print(validParentheses(s))