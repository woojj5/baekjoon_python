def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    #print(numbers)
    numbers.sort(key = lambda x: x*3, reverse  = True)
    #파이썬의 문자열의 경우 첫글자부터 비교하기 때문에, 각 문자의 원소끼리 비교하는 방식이다.
    #print(numbers)
    for i in numbers:
        answer+=i
    #print(answer)
    answer = str(int(answer))
    return answer