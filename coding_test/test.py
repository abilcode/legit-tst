import os
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

os.system('clear')

### FUNCTION
def check_x(vec):
    '''
    Checking the difference made by the coordinate on the x-axis
    or checking the delta-x
    '''
    if vec[0] > 0 :
        print(f'It moves to the right with {vec[0]} unit scale')
    elif vec[0] < 0 : 
        print(f'It moves to the left with {vec[0]} unit scale')
    else : 
        print(f'It doesn\'t move horizontaly')
    return vec[0]

def check_y(vec):
    '''
    Checking the difference made by the coordinate on the x-axis
    or checking the delta-y
    '''
    if vec[1] > 0 :
        print(f'It moves up with {vec[1]} unit scale')
    elif vec[1] < 0 : 
        print(f'It moves down with {vec[1]} unit scale')
    else :  # safety, because it's numerical process
        print(f'It doesn\'t move verticaly')
    return vec[1]

def degree(coor1,coor2):
    '''
    To calculate the degree made by 2 vector, we are going to use one of many cosine property
    which is cos(theta) = <coor1,coor2> / (<coor1,coor1>*<coor2,coor2>)**0.5.
    After that, because cosine function is invertible, we can calculate the inverse image of it by using
    arc cosine of cosine inverse
    '''
    cosine = np.dot(coor1,coor2)/((np.dot(coor1,coor1)*np.dot(coor2,coor2))**0.5)
    cosine_inverse = np.arccos(cosine)
    return np.degrees(cosine_inverse)


def plot_vector(coor1,coor2):
    '''
    Visualizing vector by each coordinate
    '''
    fig = plt.figure(figsize=(4,4))
    ax = fig.gca()
    plt.xlim([-50, 50])
    plt.ylim([-50, 50])
    plt.grid()
    ax.arrow(coor1[0], coor1[1], coor2[0], coor2[1], head_width=0.1, head_length=0.1, 
             length_includes_head=True, linewidth=2, color='r')
    plt.show()

if __name__ == "__main__":
    # container for coordinate that are considered moving
    cont_moving_vec = []
    
    # input data, feel free if you want to test another data input, it has to be int of float tho
    coordinate = {
    'x' : [0,1,2,3,-5,10,0,0,5,10,4],
    'y' : [0,0,0,4,9,-10,0,0,-6,10,-9]
    }

    # geting the constant length of each key, len(x) has to be equals to len(y), otherwise it should give you an error
    LEN = len(coordinate.get('x'))
    XAXIS = [1,0]
    viz = input('Do you want to visualized the vector ? (y/n)')
    
    for i in range(1,LEN):
       
        print(f"condition-{i}")

        # container for 2 coordinate
        coor1 = np.array([coordinate.get('x')[i-1], coordinate.get('y')[i-1]]) 
        coor2 = np.array([coordinate.get('x')[i], coordinate.get('y')[i]])
        
        # calculating vector coor2coor1 
        vec = np.array(coor2-coor1)
        
        if ((coor1 == np.array([0,0])).all() and (coor2!=np.array([0,0])).all()): 
            tetha = round(degree(XAXIS,coor2), 2)
        elif ((coor1 !=np.array([0,0])).all() and (coor2==np.array([0,0])).all()): 
            tetha = round(degree(coor1,XAXIS), 2)
        else : 
            tetha = round(degree(coor1,coor2), 2)  

        print(f'coor1 = {coor1}, coor2 = {coor2}, vec = {vec}, tetha = {tetha}')
        
        # buffer criteria
        if abs(tetha) > 15 : 
            check_x(vec)
            check_y(vec)
            cont_moving_vec.append(tuple(coor1))
            if viz == 'y':
                plot_vector(coor1,coor2)
        print('='*100)
    print("Displayed coordinate where it is considered moving : ")
    print(cont_moving_vec)

    
