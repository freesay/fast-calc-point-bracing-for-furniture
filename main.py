import tkinter as tk

window = tk.Tk()


# --- Функция расчетов --- #

def calculate():
    WIDTH = width.get()
    NUM_SHELVES = num_shelves.get()

    WIDTH = int(WIDTH)
    NUM_SHELVES = int(NUM_SHELVES)

    # roof_out and floor_out
    if variables[0].get() == 0 and variables[1].get() == 0:
        width_nom = WIDTH + 32
        space_without_shelves_nom = width_nom - ((NUM_SHELVES + 2) * 16)
        space_between_shelves_nom = space_without_shelves_nom / (NUM_SHELVES + 1)
        space_between_centers_shelves_nom = space_between_shelves_nom + 16
        point_fixing_shelf_nom = (-24)
        res_text = ''
        res_text += '---Общая информация---\n\n'
        res_text += f'Номинальная высота: {width_nom}\n'
        res_text += f'Высота пространства за вычетом полок: {round(space_without_shelves_nom, 1)}\n'
        res_text += f'Высота пространства между полками: {round(space_between_shelves_nom, 1)}\n'
        res_text += f'Расстояние между центрами полок: {round(space_between_centers_shelves_nom, 1)}\n\n'
        for i in range(NUM_SHELVES):
            point_fixing_shelf_nom += space_between_centers_shelves_nom
            res_text += f'Точка положения полки {i + 1}: {round(point_fixing_shelf_nom + 16)}\n'
            res_text += f'Точка для установки крепления {i + 1}: {round(point_fixing_shelf_nom, 1)}\n'
        print(res_text)
        text_show.config(text=f'{res_text}')

    # roof_in and floor_in
    elif variables[0].get() == 1 and variables[1].get() == 1:
        width_in = WIDTH - 32
        space_without_shelves_in = width_in - (NUM_SHELVES * 16)
        space_between_shelves_in = space_without_shelves_in / (NUM_SHELVES + 1)
        space_between_centers_shelves_in = space_between_shelves_in + 16
        point_fixing_shelf_in = (-8)
        res_text = ''
        res_text += '---Общая информация---\n\n'
        res_text += f'Номинальная высота: {width_in}\n'
        res_text += f'Высота пространства за вычетом полок: {round(space_without_shelves_in, 1)}\n'
        res_text += f'Высота пространства между полками: {round(space_between_shelves_in, 1)}\n'
        res_text += f'Расстояние между центрами полок: {round(space_between_centers_shelves_in, 1)}\n\n'
        for i in range(NUM_SHELVES):
            point_fixing_shelf_in += space_between_centers_shelves_in
            res_text += f'Точка положения полки {i + 1}: {round(point_fixing_shelf_in + 16)}\n'
            res_text += f'Точка для установки крепления {i + 1}: {round(point_fixing_shelf_in, 1)}\n'
        print(res_text)
        text_show.config(text=f'{res_text}')

    # roof_out and floor_in or roof_in and floor out
    elif variables[0].get() == 0 and variables[1].get() == 1 or \
            variables[0].get() == 1 and variables[1].get() == 0:
        width_out = WIDTH - 16
        space_without_shelves_out = width_out - (NUM_SHELVES * 16)
        space_between_shelves_out = space_without_shelves_out / (NUM_SHELVES + 1)
        space_between_centers_shelves_out = space_between_shelves_out + 16
        point_fixing_shelf_out = (-8)
        res_text = ''
        res_text += '---Общая информация---\n\n'
        res_text += f'Номинальная высота: {width_out}\n'
        res_text += f'Высота пространства за вычетом полок: {round(space_without_shelves_out, 1)}\n'
        res_text += f'Высота пространства между полками: {round(space_between_shelves_out, 1)}\n'
        res_text += f'Расстояние между центрами полок: {round(space_between_centers_shelves_out, 1)}\n\n'
        for i in range(NUM_SHELVES):
            point_fixing_shelf_out += space_between_centers_shelves_out
            res_text += f'Точка положения полки {i + 1}: {round(point_fixing_shelf_out + 16)}\n'
            res_text += f'Точка для установки крепления {i + 1}: {round(point_fixing_shelf_out, 1)}\n'
        print(res_text)
        text_show.config(text=f'{res_text}')


def clear():
    width.delete(0, 'end')
    num_shelves.delete(0, 'end')
    text_show.config(text='')


# --- Отрисовка интерфейса окна --- #

icon = tk.PhotoImage(file='icon.png')

window['bg'] = '#2b2b2b'
window.iconphoto(False, icon)
window.title('Calc Point Bracing')
window.geometry('460x640')
window.wm_attributes('-alpha', 0.95)
window.resizable(width=False, height=False)

window.grid_columnconfigure(0, minsize=220)
window.grid_columnconfigure(1, minsize=150)
window.grid_columnconfigure(2, minsize=50)

# Описание полей, кнопок и переключателей
tk.Label(window, text='Расчет точек расположения деталей\nс учетом держателей.', font=('Arial', 10),
         bg='#2b2b2b', fg='#fff').grid(row=0, columnspan=3, padx=20, pady=10)

tk.Label(window, text='Высота стойки: ', bg='#2b2b2b', fg='#fff').grid(row=1, column=0, stick='w', padx=20, pady=5)
tk.Label(window, text='Колличесто полок: ', bg='#2b2b2b', fg='#fff').grid(row=2, column=0, stick='w', padx=20, pady=5)

tk.Label(window, text='Крыша:', bg='#2b2b2b', fg='#fff').grid(row=3, column=0, padx=20, pady=10, stick='w')
tk.Label(window, text='Дно:', bg='#2b2b2b', fg='#fff').grid(row=3, column=1, padx=20, pady=10, stick='w')

tk.Label(window, text='Результат:', bg='#2b2b2b', fg='#fff').grid(row=7, column=0, padx=20, pady=5, stick='w')

# Поля ввода данных
width = tk.Entry(window, justify=tk.RIGHT, font=('Consolas', 12), bg='#3C3F41', fg='#fff')
width.grid(row=1, column=1, columnspan=2, stick='we', padx=1, pady=5)

num_shelves = tk.Entry(window, justify=tk.RIGHT, font=('Consolas', 12), bg='#3C3F41', fg='#fff')
num_shelves.grid(row=2, column=1, columnspan=2, stick='we', padx=1, pady=5)

# Переключатели
variables = [tk.IntVar() for i in range(2)]

roof_out = tk.Radiobutton(window, text='Накладная', variable=variables[0], value=0, bg='#2b2b2b', fg='#fff',
                          activebackground='#2b2b2b', activeforeground='#fff', selectcolor='#2b2b2b')
roof_out.grid(row=4, column=0, padx=20, pady=5, stick='w')

roof_in = tk.Radiobutton(window, text='Внутренняя', variable=variables[0], value=1, bg='#2b2b2b', fg='#fff',
                         activebackground='#2b2b2b', activeforeground='#fff', selectcolor='#2b2b2b')
roof_in.grid(row=5, column=0, padx=20, pady=5, stick='w')

floor_out = tk.Radiobutton(window, text='Накладное', variable=variables[1], value=0, bg='#2b2b2b', fg='#fff',
                           activebackground='#2b2b2b', activeforeground='#fff', selectcolor='#2b2b2b')
floor_out.grid(row=4, column=1, padx=20, pady=5, stick='w')

floor_in = tk.Radiobutton(window, text='Внутреннее', variable=variables[1], value=1, bg='#2b2b2b', fg='#fff',
                          activebackground='#2b2b2b', activeforeground='#fff', selectcolor='#2b2b2b')
floor_in.grid(row=5, column=1, padx=20, pady=5, stick='w')

# Кнопка калькуляции
btn_calc = tk.Button(window, height=3, text='Расчитать',
                     bg='#2b2b2b', fg='#fff', activebackground='#2b2b2b', activeforeground='#fff')
btn_calc.grid(row=6, column=0, columnspan=2, stick='we', padx=20, pady=5)
btn_calc['command'] = calculate

# Кнопка очистки
btn_clear = tk.Button(window, width=9, height=3, text='Очистить',
                      bg='#2b2b2b', fg='#fff', activebackground='#2b2b2b', activeforeground='#fff')
btn_clear.grid(row=6, column=2, stick='w', padx=2, pady=5)
btn_clear['command'] = clear

# Поле информации
text_show = tk.Label(window, text='', justify=tk.LEFT, font=('Consolas', 11), bg='#2b2b2b', fg='#fff')
text_show.grid(row=8, column=0, columnspan=3, stick='we', padx=10, pady=10)

window.mainloop()
