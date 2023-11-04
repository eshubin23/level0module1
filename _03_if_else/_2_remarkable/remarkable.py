
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    names = simpledialog.askstring(title='Name',prompt='What is your name')
    if names== 'Bob':
        messagebox.showinfo(title=None, message= "You are nice")
    elif names == "Emma":
        messagebox.showinfo(title=None, message= "you are remarkable")
    elif names == "Joe":
        messagebox.showinfo(title=None, message= "you are kind")
