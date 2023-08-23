import tkinter as tk
import json
import os

# Инициализация флагов для отслеживания открытия пунктов меню
routes_opened = False
tickets_opened = False
items_opened = False
budget_opened = False
add_route_window_opened = False
add_ticket_window_opened = False
add_item_window_opened = False



# Функция для сохранения данных в JSON файл
def save_data_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)

# Функция для загрузки данных из JSON файла
def load_data_from_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

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

        routes = load_data_from_json("data.json")  # Загрузка данных из файла
        for route in routes:
            routes_listbox.insert(tk.END, f"{route['from']} - {route['to']}")

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
                        routes.append(route)
                        save_data_to_json(routes, "data.json")
                        routes_listbox.insert(tk.END, f"{route['from']} - {route['to']}")
                        add_route_window.destroy()

                save_button = tk.Button(add_route_window, text="Сохранить", command=save_route)
                save_button.pack()

        add_button = tk.Button(routes_window, text="Добавить маршрут", command=add_route)
        add_button.pack()

        routes_opened = True

# Функция которая добавляет функционал кнопке "Билеты"
def open_tickets():
    global tickets_opened
    if not tickets_opened:
        tickets_window = tk.Toplevel(root)
        tickets_window.title("Билеты")

        tickets_label = tk.Label(tickets_window, text="Сохраненные билеты:")
        tickets_label.pack()

        tickets_listbox = tk.Listbox(tickets_window)
        tickets_listbox.pack()

        tickets = load_data_from_json("data.json")
        for ticket in tickets:
            tickets_listbox.insert(tk.END, f"Откуда: {ticket['from']} - Куда: {ticket['to']}")

        def add_ticket():
            global add_ticket_window_opened
            if not add_ticket_window_opened:
                add_ticket_window = tk.Toplevel(tickets_window)
                add_ticket_window.title("Добавить билет")
                add_ticket_window_opened = True

                from_label = tk.Label(add_ticket_window, text="Откуда:")
                from_label.pack()

                from_entry = tk.Entry(add_ticket_window)
                from_entry.pack()

                to_label = tk.Label(add_ticket_window, text="Куда:")
                to_label.pack()

                to_entry = tk.Entry(add_ticket_window)
                to_entry.pack()

                time_label = tk.Label(add_ticket_window, text="Время:")
                time_label.pack()

                time_entry = tk.Entry(add_ticket_window)
                time_entry.pack()

                name_label = tk.Label(add_ticket_window, text="Имя:")
                name_label.pack()

                name_entry = tk.Entry(add_ticket_window)
                name_entry.pack()

                surname_label = tk.Label(add_ticket_window, text="Фамилия:")
                surname_label.pack()

                surname_entry = tk.Entry(add_ticket_window)
                surname_entry.pack()

                class_label = tk.Label(add_ticket_window, text="Класс:")
                class_label.pack()

                class_entry = tk.Entry(add_ticket_window)
                class_entry.pack()

                def save_ticket():
                    from_place = from_entry.get()
                    to_place = to_entry.get()
                    ticket_time = time_entry.get()
                    ticket_name = name_entry.get()
                    ticket_surname = surname_entry.get()
                    ticket_class = class_entry.get()
                    if from_place and to_place and ticket_time and ticket_name and ticket_surname and ticket_class:
                        ticket = {
                            "from": from_place,
                            "to": to_place,
                            "time": ticket_time,
                            "name": ticket_name,
                            "surname": ticket_surname,
                            "class": ticket_class
                        }
                        tickets.append(ticket)
                        save_data_to_json(tickets, "data.json")
                        tickets_listbox.insert(tk.END, f"Откуда: {ticket['from']} - Куда: {ticket['to']} - Время: {ticket['time']} - Имя: {ticket['name']} - Фамилия: {ticket['surname']} - Класс: {ticket['class']}")
                        add_ticket_window.destroy()

                save_button = tk.Button(add_ticket_window, text="Сохранить", command=save_ticket)
                save_button.pack()

        add_button = tk.Button(tickets_window, text="Добавить билет", command=add_ticket)
        add_button.pack()

        tickets_opened = True

# Функция которая добавляет функционал кнопке "Список вещей"
def open_items():
    global items_opened
    if not items_opened:
        items_window = tk.Toplevel(root)
        items_window.title("Список вещей")

        items_label = tk.Label(items_window, text="Список вещей:")
        items_label.pack()

        global items_listbox
        items_listbox = tk.Listbox(items_window)
        items_listbox.pack()

        def refresh_items_listbox():
            items_listbox.delete(0, tk.END)
            with open("data.json", "r") as file:
                items = json.load(file)
                for item in items:
                    items_listbox.insert(tk.END, item)

        refresh_items_listbox()

        def add_item():
            global add_item_window_opened
            if not add_item_window_opened:
                add_item_window = tk.Toplevel(items_window)
                add_item_window.title("Добавить вещь")
                add_item_window_opened = True

                item_label = tk.Label(add_item_window, text="Вещь:")
                item_label.pack()

                global item_entry
                item_entry = tk.Entry(add_item_window)
                item_entry.pack()

                def save_item():
                    item = item_entry.get()
                    if item:
                        add_item_to_json(item)
                        refresh_items_listbox()  # Обновляем список вещей после добавления
                        add_item_window.destroy()

                save_button = tk.Button(add_item_window, text="Сохранить", command=save_item)
                save_button.pack()

        add_button = tk.Button(items_window, text="Добавить вещь", command=add_item)
        add_button.pack()

        items_opened = True

        # Функция для добавления вещи в JSON файл
        def add_item_to_json(item):
            if not os.path.exists("data.json"):
                with open("data.json", "w") as file:
                    json.dump([], file)

            with open("data.json", "r") as file:
                items = json.load(file)

            items.append(item)

            with open("data.json", "w") as file:
                json.dump(items, file)

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

# Размеры создаваемого окна
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Создание кнопок и их действий
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

items_listbox = tk.Listbox(root)
items_listbox.pack()

root.mainloop()

