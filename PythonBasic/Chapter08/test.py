import os
print(os.getcwd())

try :
    ftest = open('./ftest.txt', mode='r')
    print(ftest.read())
except Exception as e :
    print(f'Error 발생 {e}')

finally:
    ftest.close()