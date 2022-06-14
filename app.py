from model import Model
from view import View
from controller import Controller
from tkinter import Tk

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Soccer League Manager')
        self.geometry('500x500')
        
        model = Model()
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(model, view)
        
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()