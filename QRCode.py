import io
import pyqrcode
from base64 import b64encode
import eel

eel.init('web')
def code(data):
    import numpy as np
    from numpy import ma
    import matplotlib.pyplot as plt

    s1 = data
    if s1[0] == '0':
        s = '0' + s1
    elif s1[0] == '1':
        s = '1' + s1
    y = []
    for i in s:
        y.append(int(i))
    print(y)    
    x = np.arange(0, len(y), 1)
    y = np.array(y)
    print ("NRZ")
    print(y)
    print(x)

    plt.step(x, y, label='NRZ')

    y2 = []
    for i in y:
        if int(i) == 0:
            y2.append(1)
            y2.append(0)
        elif int(i) == 1:
            y2.append(0)
            y2.append(1)
    x2 = np.arange(-0.5, len(y)-0.5, 0.5)

    for i in range(len(x2)):
        plt.vlines(i*0.5, 0, 10,
            color = 'black',    #  цвет
            linewidth = ((i+1) % 2) + 0.5,    #  ширина
            linestyle = ':')    #  начертание 
        
    plt.hlines(2, 0, len(x) - 1,
            color = 'black',    #  цвет
            linewidth = 2,    #  ширина
            linestyle = '-')    #  начертание 
    plt.hlines(4, 0, len(x) - 1,
            color = 'black',    #  цвет
            linewidth = 2,    #  ширина
            linestyle = '-')    #  начертание
    plt.hlines(0, 0, len(x) - 1,
            color = 'black',    #  цвет
            linewidth = 0.5,    #  ширина
            linestyle = '-')    #  начертание

    print("Манчестерский")
    print(y2)
    print(x2)
    for i in range(len(y2)):
        y2[i] += 2
    y2 = np.array(y2)
    print(y2)
    print(x2)
    plt.step(x2, y2, label='Манчестерский')

    plt.legend()
    plt.xlim(0, len(y) + 1)
    plt.ylim(min(y), max(y) + 4)

    print("AMI")
    x3 = x
    y3 = []
    count = 0
    for i in y:
        if int(i) == 0:
            y3.append(i * 0.5)
        elif int(i) == 1 and count == 0:
            y3.append(i * 0.5)
            count += 1
        elif int(i) == 1 and count > 0:
            y3.append(-i * 0.5)
            count = 0
    for i in range(len(y)):
        y3[i] += 4
        
    print(y3)
    print(x3)
    print(len(x3))
    print(len(y3))
    y3 = np.array(y3)
    plt.step(x3, y3, label = 'AMI')
    plt.savefig('web/foo.png')
    plt.show()
    return "Hello"

@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}


@eel.expose
def generate_qr(data):
    img = code(data)
    print(type(data))
    '''buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")'''
    return "data:image/png;base64, " + img #encoded 



eel.start('index.html', size=(1000, 600))
