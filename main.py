import tkinter as tk
import json
import os

# Инициализация флагов для отслеживания открытия пунктов меню
routes_opened = False
tickets_opened = False
items_opened = False
budget_opened = False
add_route_window_opened = False

# Функция которая добавляет функционал кнопке "Маршруты"
def open_routes():
    global routes_opened
    if not routes_opened:
        routes_window = tk.Toplevel(root)
        routes_window.title("Маршруты")

        routes_label = tk.Label(routes_window, text="Сохраненные маршруты:")
        routes_label.pack()

        routes_listbox = tk.Listbox(routes_window)
        routes_listbox.pack()

        with open("routes.json", "r") as file:
            routes = json.load(file)
            for route in routes:
                routes_listbox.insert(tk.END, f"{route['from']} - {route['to']}")

        # Функция которая добавляет функционал кнопке "Добавить маршруты"
        def add_route():
            global add_route_window_opened
            if not add_route_window_opened:
                add_route_window = tk.Toplevel(routes_window)
                add_route_window.title("Добавить маршрут")
                add_route_window_opened = True

            from_label = tk.Label(add_route_window, text="Откуда:")
            from_label.pack()

            from_entry = tk.Entry(add_route_window)
            from_entry.pack()

            to_label = tk.Label(add_route_window, text="Куда:")
            to_label.pack()

            to_entry = tk.Entry(add_route_window)
            to_entry.pack()

            def save_route():
                from_place = from_entry.get()
                to_place = to_entry.get()
                if from_place and to_place:
                    route = {"from": from_place, "to": to_place}
                    save_route_to_json(route)
                    routes_listbox.insert(tk.END, f"{route['from']} - {route['to']}")
                    add_route_window.destroy()

            save_button = tk.Button(add_route_window, text="Сохранить", command=save_route)
            save_button.pack()

        add_button = tk.Button(routes_window, text="Добавить маршрут", command=add_route)
        add_button.pack()

        routes_opened = True

# Функция которая создаёт файл .json
def save_route_to_json(route):
    global routes_opened
    if not os.path.exists("routes.json"):
        with open("routes.json", "w") as file:
            json.dump([], file)

    with open("routes.json", "r") as file:
        routes = json.load(file)

    routes.append(route)

    with open("routes.json", "w") as file:
        json.dump(routes, file)

# Функция которая добавляет функционал кнопке "Билеты"
def open_tickets():
    global tickets_opened
    if not tickets_opened:
        tickets_window = tk.Toplevel(root)
        tickets_window.title("Билеты")



        tickets_opened = True

# Функция которая добавляет функционал кнопке "Список вещей"
def open_items():
    global items_opened
    if not items_opened:
        items_window = tk.Toplevel(root)
        items_window.title("Список вещей")



        items_opened = True

# Функция которая добавляет функционал кнопке "Бюджет"
def open_budget():
    global budget_opened
    if not budget_opened:
        budget_window = tk.Toplevel(root)
        budget_window.title("Бюджет")



        budget_opened = True
# Функция которая добавляет функционал кнопке "Планирование поездки"
def exit_program():
    root.quit()

root = tk.Tk()
root.title("Планирование поездки")

# Розмеры создаваемого окна
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Создание кнопоко и их действия
routes_button = tk.Button(root, text="Маршруты", command=open_routes)
tickets_button = tk.Button(root, text="Билеты", command=open_tickets)
items_button = tk.Button(root, text="Список вещей", command=open_items)
budget_button = tk.Button(root, text="Бюджет", command=open_budget)
exit_button = tk.Button(root, text="Выход", command=exit_program)

# Отображение кнопок в окне
routes_button.pack()
tickets_button.pack()
items_button.pack()
budget_button.pack()
exit_button.pack()

root.mainloop()
