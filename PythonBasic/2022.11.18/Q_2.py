"""
메시지.txt 파일 생성 -> try catch
파일에 메시지 입력 : 파이팅
10번 돌림
"""

try:
    with open('//192.168.0.47/데이터분석_수업/박종민/2022.11.18/메세지.txt', mode='w', encoding='UTF-8') as wtext :
        for i in range(1,11) :
            wtext.write(f'파이팅{i}\n')
except Exception as e:
    print(f'error {e}')


