from gui import *


def main():
    window = Tk()
    window.title('Project 2')
    window.geometry('450x350')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
