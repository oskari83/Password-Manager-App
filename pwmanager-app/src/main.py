#from app import PasswordManagerApp
from tkinter import Tk
from ui.ui import UI
from ttkthemes import ThemedTk

def main():
    window = ThemedTk(theme="breeze")
    window.title("Password Manager")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
