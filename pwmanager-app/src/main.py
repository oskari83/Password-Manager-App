from ttkthemes import ThemedTk
from ui.ui import UI

def main():
    """Sovelluksen main funktio joka luo Tkinter ikkunan, ja
    käynnistää käyttöliittymän (eli käynnistää sovelluksen).
    """

    window = ThemedTk(theme="breeze")
    window.title("Password Manager")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
