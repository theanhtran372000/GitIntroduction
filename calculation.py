from cgitb import reset
import math

def cal_rectangle_perimeter(a, b):
    return 2 * (a + b)

if __name__ == '__main__':
    f = int (input('''
        Choose your function:
            0. Calculate rectangle perimerter
            
        Your choice: '''))
    
    if f == 0:
        a = int(input("Input a = "))
        b = int(input("Input b = "))
        
        result = cal_rectangle_perimeter(a, b)
        
    print('Result: {}'.format(result))