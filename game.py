import time
from tkinter import *
from tkinter import messagebox
from logic import *

tk = Tk()
app_running = True
# Размер холста
size_canvas_x = 500
size_canvas_y = 500

s_x = s_y = 10  # Размер игрового поля
step_x = size_canvas_x // s_x  # Шаг по горизонтали
step_y = size_canvas_y // s_y  # Шаг по вертикали
size_canvas_x = step_x * s_x # Вычисление новых размеров холста
size_canvas_y = step_y * s_y # Вычисление новых размеров холста
menu_x = 250 # Размер области меню
ships = s_x // 2 # определяем максимальное количество кораблей
# Определяем длинну кораблей
ship_len1 = s_x // 5
ship_len2 = s_x // 3
ship_len3 = s_x // 2

enemy_ships = [[0 for i in range(s_y + 1)] for i in range(s_x + 1)]
list_ids = []

def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()


def draw_table():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Морской бой")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
canvas.update()

draw_table()


def button_show_enemy():
    pass


def button_begin_again():
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships[j][i] > 0:
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                              fill="red")
                list_ids.append(_id)


b0 = Button(tk, text="Показать корабли противника", command=button_show_enemy)
b0.place(x=size_canvas_x + 20, y=30)

b1 = Button(tk, text="Начать заново!", command=button_begin_again)
b1.place(x=size_canvas_x + 20, y=70)


def add_to_all(event):
    _type = 0  # ЛКМ
    if event.num == 3:
        _type = 1  # ПКМ
    # print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    # print(ip_x, ip_y, "_type:", _type)


canvas.bind_all("<Button-1>", add_to_all)  # ЛКМ
canvas.bind_all("<Button-3>", add_to_all)  # ПКМ
enemy_ships = generate_enemy_ships(ship_len1, ship_len2, ship_len3, ships, s_x, s_y)

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)