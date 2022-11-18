# 2.

try:
    text = open('./test.txt', mode='a')

    while True :

        input_text = input('저장할 내용을 입력하세요 (종료는 엔터)\n')

        if input_text == "":
            break
        text.write(input_text+'\n')

    text = open('./test.txt', mode='r')
    print(text.readlines())
except Exception as e :
    print(f'Error 발생 {e}')
finally:
    text.close()

