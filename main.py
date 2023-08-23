import tkinter as tk
import json
import os

def open_routes():
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

    def add_route():
        add_route_window = tk.Toplevel(routes_window)
        add_route_window.title("Добавить маршрут")

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

def open_tickets():
    tickets_window = tk.Toplevel(root)
    tickets_window.title("Билеты")

    # Добавьте код для отображения билетов

def open_items():
    items_window = tk.Toplevel(root)
    items_window.title("Список вещей")

    # Добавьте код для отображения списка вещей

def open_budget():
    budget_window = tk.Toplevel(root)
    budget_window.title("Бюджет")

    # Добавьте код для отображения бюджета

# Остальной код остается таким же

root = tk.Tk()
root.title("Планирование поездки")

window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

routes_button = tk.Button(root, text="Маршруты", command=open_routes)
tickets_button = tk.Button(root, text="Билеты", command=open_tickets)
items_button = tk.Button(root, text="Список вещей", command=open_items)
budget_button = tk.Button(root, text="Бюджет", command=open_budget)

routes_button.pack()
tickets_button.pack()
items_button.pack()
budget_button.pack()

root.mainloop()
