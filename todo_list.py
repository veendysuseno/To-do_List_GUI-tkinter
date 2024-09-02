import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan tugas
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Fungsi untuk menghapus tugas
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Fungsi untuk menghapus semua tugas
def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Membuat jendela utama
root = tk.Tk()
root.title("To-Do List")

# Membuat frame untuk menampung widget
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

# Scrollbar untuk daftar tugas
scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox untuk menampilkan daftar tugas
listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, yscrollcommand=scrollbar_tasks.set)
listbox_tasks.pack(side=tk.LEFT)

# Konfigurasi scrollbar
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry untuk memasukkan tugas baru
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Button untuk menambahkan tugas
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

# Button untuk menghapus tugas
button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(pady=5)

# Button untuk menghapus semua tugas
button_clear_tasks = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
button_clear_tasks.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
