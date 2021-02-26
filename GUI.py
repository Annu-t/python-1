import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("AppFolder")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)

    for app in apps:
        label = tk.Label(frame, text=app, bg="pink")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=600, width=600, bg="#178000")
canvas.pack()

frame = tk.Frame(root, bg="olive")
frame.place(relwidth=0.8, relheight=0.9, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", width=80, padx=25, pady=10, fg="black", bg="#d9471a", command=addApp)

openFile.pack()
runApps = tk.Button(root, text="Run Apps", width=80, padx=25, pady=10, fg="black", bg="#522d2d", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
