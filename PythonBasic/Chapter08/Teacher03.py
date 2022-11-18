#3

try:
    re_text = open('./life.txt', mode='w')
    re_text.write('Life is too short\n you need python')
    re_text = open('./life.txt', mode='r')
    print(re_text.read())
except Exception as e :
    print(f'Error 발생 {e}')
finally:
    pass