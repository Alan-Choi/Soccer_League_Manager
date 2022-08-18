from model import Model
# from view import View
from controller import Controller
from tkinter import Tk
from view2 import MyGUI
from PyQt5.QtWidgets import QApplication

class App():
    def __init__(self):
        super().__init__()
        
        # self.title('Soccer League Manager')
        # self.geometry('500x500')
        
        model = Model()
        
        # view = View(self)
        app = QApplication([])
        view = MyGUI()
        
        controller = Controller(model, view)
        controller.initialize_database()
        
        view.show()
        app.exec_()
        # view.grid(row=0, column=0, padx=10, pady=10)

        
        # view.set_controller(controller)

def main():
    App()
    
    
if __name__ == '__main__':
    main()
    # app.mainloop()