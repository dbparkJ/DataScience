var=10
#들여쓰기(Indentation)으로 블럭을 표현
if var>=5 :
    print('var=',var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

print('항상 실행')
print('')
"""
여러줄 주석의 효과를 낼 수 있다
컨트롤 +/ 하면 주석처리
"""
if var>=5 :
    #print('var=',var) <- if 이하의 블럭은 동일한 들여쓰기 개수로 작성 해야 한다.
    print('var=',var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
print('항상실행')
print('')
if var>=100:
    print('var=', var)
    print('var는 3보다 작다.')
    print('조건이 참인 경우 실행')
