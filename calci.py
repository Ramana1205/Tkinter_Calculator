import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="pink")
root.resizable(False, False)

entry = tk.Entry(
    root,
    width=40,
    borderwidth=5,
    font=("Arial",16),
    bg="white",
    fg="black",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "FUCK YOU")

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r = 1
c = 0

for b in buttons:
    if b == "=":
        tk.Button(root, text=b, width=10, height=2,bg="black",fg="white",
                  command=calc).grid(row=r, column=c)
    else:
        tk.Button(root, text=b, width=10, height=2,bg="white",fg="red",
                  command=lambda x=b: press(x)).grid(row=r, column=c)

    c += 1
    if c > 3:
        c = 0
        r += 1

tk.Button(root, text="Clear", width=42, height=2,bg="red",fg="white",padx=20,pady=20,
          command=clear).grid(row=r+1, column=0, columnspan=4)

root.mainloop()
