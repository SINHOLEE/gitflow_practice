def solution(new_id):
    #1
    answer = new_id.lower()
    #2
    temp = ""
    for c in answer:
        if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')) or ord(c) in [ord('-'), ord('_'), ord('.')]:
            temp += c
    answer = temp
    #3
    old_answer = ""
    while answer != old_answer:
        old_answer = answer
        answer = answer.replace("..", '.')
    #4
    if len(answer) > 0 and answer[0] ==  '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    #5
    if answer == "":
        answer = 'a'
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if (answer[-1] ==  '.'):
            answer = answer[:-1]
    #7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("z-+.^."))


