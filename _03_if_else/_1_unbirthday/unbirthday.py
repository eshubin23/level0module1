
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
     window = Tk()
     window.withdraw()
    birthday = simpledialog.askstring(title='Birthday or not',prompt='When is your birthday')
    if birthday== "11/03":
        messagebox.showinfo(title=None, message= "Happy Birthday")
    else:
        messagebox.showinfo(title=None, message= "Happy Unbirthday")
