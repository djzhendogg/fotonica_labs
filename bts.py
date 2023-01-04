from tkinter import *
import random
import time

import numpy as np

import tkinter.font as font

root = Tk()
root.geometry('600x600')
root.title('Время реакции')

text = 'в центре экрана монитора в случайном порядке предъявляется\nцифры натурального ряда (от 0 до 9), которые вы должены\nклассифицировать по следующему простому алгоритму:\nпри появлении чётной цифры\nреагировать нажатием на левую кнопку мыши,\n при проявлении нечётной на правую кнопку мыши.\n Нажатие на кнопки непрерывно меняет цифру на экране.\nСначала нажмите ОК чтобы закрыть правила.\nНажмите на старт, чтобы начать.\nКак только исчезнет "reaction check" появится первая цифра'


label1 = Label(root, text = "задача на устойчивость зрительного внимания", font = ("Arial", 10))
lable2 = Label(root, text = text, font = ("Arial", 11))

label1.pack()
lable2.pack()


right_even = []
false_even = []
right_odd = []
false_odd = []
dur_list = []


lable3 = Label(root, text = "<<>>><>>>")
lable4 = Label(root, text = "reaction check")
lable5 = Label(root, text = "<<>>><>>>")



numbers = random.sample(range(10), 10)

def ya_ponyal(bbb):
    lable2.destroy()
    bbb.destroy()
    lable3.pack()
    lable4.pack()
    lable5.pack()



b_ok = Button(root, text = "OK", command=lambda: ya_ponyal(b_ok))
b_ok.pack()



def ugadai_chetnoct(beka):

    # lable2.destroy()
    time.sleep(2)
    lable3.destroy()
    lable4.destroy()
    lable5.destroy()
    for i in numbers:

        var = IntVar()
        # lable4.pack()
        # time.sleep(1)
        
        def even_num(num, lab6, var):
            end = time.time()
            if num%2 == 0:
                right_even.append(num)
            else:
                false_even.append(num)
            # butti.destroy()
            duration = round(end - start, 4)
            dur_list.append(duration)
            lable7 = Label(root, text = 'время реакции' + str(duration), width=20, height=2)
            # lable7.pack()
            lab6.destroy()
            var = var.set(1)
            # return lable7

        def odd_num(num, lab6, var):
            end = time.time()
            if num%2 != 0:
                right_odd.append(num)
            else:
                false_odd.append(num)
            # butti.destroy()
            duration = round(end - start, 4)
            dur_list.append(duration)
            lable7 = Label(root, text = 'время реакции' + str(duration), width=20, height=1)
            # lable7.pack()
            lab6.destroy()
            var = var.set(1)
            return lable7
        # var = 1
        lable6 = Label(root, text = str(i), width=10, height=10, font='Times 30')
        lable6.pack()
        lable6.bind('<Button-1>',lambda event: even_num(i, lable6, var))
        lable6.bind('<Button-3>',lambda event: odd_num(i, lable6, var))
        # root.after(6000, lable6.destroy)
        start = time.time()
        lable6.wait_variable(var)
        # def clening(
        #             # l1, l2, l3, 
        #             l6, var, buty):
        #     # l1.pack_forget()
        #     # l2.pack_forget()
        #     # l3.pack_forget()
        #     l6.destroy()
        #     # l7.destroy()
        #     var = var.set(2)
        #     buty.destroy()
        lable6.destroy()
        #             # l7.destroy()
        #             # var = var.set(2)
        # buty.destroy()
        # b = Button(root, text="четный", command=lambda: even_num(i, b, lable6))
        # b.pack()
        # # b.wait_variable()
        # b.bind('<Return>', even_num(i, b, lable6))        
        # b.grid(row=3,column=0)



        # cleaning_b = Button(root, text="Next", command=lambda: clening(
        #                                                         # l1, l2, l3, 
        #                                                         lable6, var, cleaning_b))

        # cleaning_b.pack()
        # cleaning_b.wait_variable(var)
        
    closeeer = Label(root, text = "Закройте окно для получения результата", font = ("Arial", 15))
    closeeer.pack()



# for i in numbers:
#     b_to_start = Button(root, text = "клик ту старт", command=lambda: ugadai_chetnoct(i, b_to_start))
#     b_to_start.pack()
    # print(b_to_start)

    # b_to_start.wait_variable()
myFont = font.Font(size=20)
b_to_start = Button(root, text = "клик ту старт", command=lambda: ugadai_chetnoct(b_to_start), font = myFont)

b_to_start.pack()
lable3.pack()
lable4.pack()
lable5.pack()




root.mainloop()
print(len(right_even), len(right_odd), len(false_even), len(false_odd))
print(numbers)
print(right_even)
print(right_odd)
print(false_odd)
print(false_even)
print(dur_list)

dur_arr = np.array(dur_list)

tsr = np.mean(dur_arr)
N = 10
C = len(false_even) + len(false_odd)

tisum = np.sum(abs(dur_arr - tsr))

uv = np.round((N/(N-C))*tisum/tsr, 3)
win = Tk()
win.geometry('600x200')
win.title('Время реакции')

result = Label(win, text = "Ваша устойчивость зрительного внимания: " + str(uv), font = ("Arial", 15))
result.place(anchor="center")

result.pack()
win.mainloop()