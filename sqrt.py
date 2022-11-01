import math

def quadratic(a, b, c):
    DT=b*b-4*a*c
    if DT<0:
        print('此方程无解')
    else :
        return  (math.sqrt(DT)-b)/(2*a),(-math.sqrt(DT)-b/(2*a))
    
print(quadratic(1,3,2))
    