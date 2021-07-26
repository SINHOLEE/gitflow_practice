def decime_to_ternary_list(n):
    s = ""
    while n:
        s += str(n % 3)
        n = n // 3
    return list(reversed(list(s)))


def has_zero(ternary_list):
    for item in ternary_list:
            if (item == "0"):
                return True
    return False


def remove_zero_recursive(ternary_list):
    # base case '0'이 없을때까지 반복
    if (not has_zero(ternary_list)):
        return ternary_list

    ternary_list = ternary_list[:]
    for i in range(len(ternary_list)):
        if (ternary_list[i] == "0"):
            # 맨 앞에 0 이있으면 지우고
            if (i == 0):
                ternary_list[i] = ""
                continue
            # 그 외의 0은 앞자리가 1,2,4중 하나이므로 각각 알맞게 변환하라
            ternary_list[i] = '4'
            if ternary_list[i - 1] == '1':
                ternary_list[i-1]="0"
            elif ternary_list[i - 1] == '2':
                ternary_list[i-1] = '1'
            elif ternary_list[i - 1] == '4':
                ternary_list[i-1] = '2'
    return remove_zero_recursive(ternary_list)

# 3진법으로 변환 후 3에 해당하는 10을 상황별로 처리하는 로직
def solution(n):
    answer = ''
    ternary = remove_zero_recursive(decime_to_ternary_list(n))
    return ''.join(ternary)



for i in range(100):
    print(i, decime_to_ternary_list(i), solution(i))