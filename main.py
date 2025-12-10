from tkinter import *
from gui import GUI


def main() -> None:
    """
    Start the voting application.
    """
    window = Tk()
    window.title("VOTING APPLICATION")
    window.geometry("350x320")

    GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
