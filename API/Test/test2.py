import time

continue_loop = True

while continue_loop:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print(f'{a} + {b} = {a+b}')

        st = input(('continue (y/n) : '))
        
        while True:
            if st == 'n':
                continue_loop = False
                break
            elif st == 'y':
                break
            else:
                st = input(('continue (y/n) : '))

        print('--'*40)
    except ValueError:
        print('Lỗi dữ liệu, vui lòng nhập lại')
        print('--'*40)
