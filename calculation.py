from cgitb import reset
import math

def cal_rectangle_perimeter(a, b):
    return 2 * (a + b)

def cal_circle_area(r):
    return math.pi * math.pow(r, 2)

if __name__ == '__main__':
    f = int (input('''
        Choose your function:
            0. Calculate rectangle perimerter
            1. Calculate circle area
            
        Your choice: '''))
    
    if f == 0:
        a = int(input("Input a = "))
        b = int(input("Input b = "))
        
        result = cal_rectangle_perimeter(a, b)
        
    elif f == 1:
        r = int(input('Input r: '))
        
        result = cal_circle_area(r)
    
    print('Result: {}'.format(result))