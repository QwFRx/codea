'''
#  сортировка списка кортеджей по указанному элементу

a = [(234, False, "Влад"), (45, True, "Иван")]
a.sort(key = lambda x:x[2])
print(a)
'''


'''
# отсортировать НЕчетные элементы списка
numbers = list(range(10))
chet = list(filter(lambda x:x % 2 != 0, numbers))
print(chet)
'''


'''
import tkinter
root = tkinter.Tk()
root.title('lambda')
a = 0
tkinter.Button(root, text = 'нажми меня', command = lambda: print('КНОПКА НАЖАТА')).pack()

root.mainloop()
'''

# программа, которая определяет весокосный год или нет
ye = int(input('Введите год: '))
def visokosn(ye):
    if ye % 4 == 0 or ye % 40 == 0:
        print(f'{ye} високосный')
    else:
        print(f'{ye} не високосный')

visokosn(ye)