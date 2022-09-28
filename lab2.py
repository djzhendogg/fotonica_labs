import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import pi
import pandas as pd
from scipy import integrate

# our function
def f(x):
    return sin(2 * pi * x)

fArea,err = integrate.quad(f,0,2* pi)
# print("Integral area:",fArea)



# NewtonCotes method
matrix_weight = np.array([[1, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0, 0],
                   [1, 4, 1, 0, 0, 0],
                   [1, 3, 3, 1, 0, 0],
                   [7, 32, 12 , 32, 7, 0],
                   [19,75, 50, 50, 75, 19]])
Cn = [1, 2, 6, 8, 90, 288]


# N - number of partial segments
# n - order of the method
# j - partial segment index
# i - point index on the partial segment


N = range(100, 10000, 100)
a = 0
b = 2* pi
ans_all = pd.DataFrame()
n = range(1, 6)
for y in n:
    part_cuts = []
    answ_res = []
    for k in N:
        h = (b-a)/k/y
        before = h*y/Cn[y]
        xi = a
        sum = 0
        xj = a
        part_cuts.append(k)
        for j in range(1, k+1):
            for i in range(y+1):
                sum += matrix_weight[y][i]*f(xi)
                xi = xj + i*h
            xj = xj + y*h
        ans = sum*before
        answ_res.append(ans)
    converted_num = str(i)
    ans_all['in' + converted_num + 'number of pc'] = part_cuts
    ans_all['in' + converted_num + 'results'] = answ_res
    ans_all['accur' + converted_num] = fArea - ans_all['in' + converted_num + 'results']
    plt.plot(ans_all['in' + converted_num + 'number of pc'], ans_all['accur' + converted_num], label= converted_num + ' ' + 'порядок')
plt.xlabel('number of pc')
plt.ylabel('eror')
plt.legend(loc="upper right")
plt.title('Зависимости точности от шага для метода Ньютона-Котеса')
plt.show()

# Gauss method
xi11_1 = [0]
xi11_2 = [-0.5773503, 0.5773503]
xi11_3 = [-0.7745967, 0, 0.7745967]
xi11_4 = [-0.8611363, -0.3399810, 0.3399810, 0.8611363]
xi11_5 = [-0.9061798,	-0.5384693,	0,	 0.5384693,	 0.9061798]
xi11_6 = [-0.9324700,	-0.6612094,	-0.2386142,	 0.2386142,	 0.6612094,	 0.9324700]

ci_1 = [2]
ci_2 = [1, 1]
ci_3 = [0.5555556, 0.8888889,	0.5555556]
ci_4 = [0.3478548,	0.6521451,	0.6521451,	0.3478548]
ci_5 = [0.4786287,	0.2369269,	0.5688888,	0.2369269,	0.4786287]
ci_6 = [0.1713245,	0.3607616,	0.4679140,	0.4679140,	0.3607616,	0.1713245]


# N - number of partial segments
# n - order of the method
# j - partial segment index
# i - point index on the partial segment

N = range(100, 10000, 100)
a = 0
b = 2* pi
ans_all = pd.DataFrame()
n = range(1, 7)

for y in n:
    part_cuts = []
    answ_res = []
    for k in N:
        h = (b-a)/k
        before = (b-a)/k/2
        sum = 0
        xj_1 = a
        part_cuts.append(k)
        for j in range(1, k+1):
            for i in range(y):
                if y == 1:
                    xi = xj_1 + (xi11_1[i] + 1)*(h)/2
                    sum += ci_1[i]*f(xi)
                if y == 2:
                    xi = xj_1 + (xi11_2[i] + 1)*(h)/2
                    sum += ci_2[i]*f(xi)
                if y == 3:
                    xi = xj_1 + (xi11_3[i] + 1)*(h)/2
                    sum += ci_3[i]*f(xi)
                if y == 4:
                    xi = xj_1 + (xi11_4[i] + 1)*(h)/2
                    sum += ci_4[i]*f(xi)
                if y == 5:
                    xi = xj_1 + (xi11_5[i] + 1)*(h)/2
                    sum += ci_5[i]*f(xi)
                if y == 6:
                    xi = xj_1 + (xi11_6[i] + 1)*(h)/2
                    sum += ci_6[i]*f(xi)
            xj_1 = xj_1 + h
        ans = sum*before
        answ_res.append(ans)
    converted_num = str(i)
    ans_all['in' + converted_num + 'number of pc'] = part_cuts
    ans_all['in' + converted_num + 'results'] = answ_res
    ans_all['accur' + converted_num] = abs(fArea - ans_all['in' + converted_num + 'results'])
    plt.plot(ans_all['in' + converted_num + 'number of pc'], ans_all['accur' + converted_num], label= converted_num + ' ' + 'порядок')
plt.xlabel('number of pc')
plt.ylabel('eror')
plt.legend(loc="upper right")
plt.title('Зависимости точности от шага для метода Гауса')
plt.show()


# Point spread function
characters = []

fh = open(r"C:\Users\1665865\PycharmProjects\matlabb\psf_c20_03.txt" , 'r') # fh is short for "file_handle."

for line in fh:
    characters.append(line.strip()) # strip() removes the newline characters

fh.close() # This is important!

for i in range(len(characters)):
    input_1 = characters[i]
    arr = [float(x) for x in input_1.split(' ')]
    characters[i] = arr
frt = np.array(characters)
k = frt[:,128]
x = np.arange(-6.375, 6.380, 0.05)

plt.plot(x, k, color="red")
plt.title('Сечение ФРТ')
plt.show()


# Energy Concentration Function
x = np.arange(-6.375, 6.380, 0.05)
y = np.arange(-6.375, 6.380, 0.05)
r = np.arange(0, 6.380, 0.05)
full_ener = 0
for i in range(len(x)):
    for j in range(len(y)):
        full_ener += frt[i][j]

fki_of_r = pd.DataFrame()

fki_list = []
radii = []
for k in range(len(r)):
    r_ener = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]**2 + y[i]**2 <= r[k]**2:
              r_ener += frt[j][i]
            fki = r_ener/full_ener
    fki_list.append(fki)
    radii.append(r[k])
fki_of_r['fki'] = fki_list
fki_of_r['radii'] = radii
plt.plot(fki_of_r['radii'], fki_of_r['fki'], color="red")
plt.title('ФКЭ')
plt.show()