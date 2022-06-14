from ctypes import alignment
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import Canvas
from PIL import ImageTk, Image

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = Canvas(self, width=100, height=100, bg= 'white', highlightbackground='black', highlightthickness=1)
        self.canvas.grid(row=2, column=1)
        self.label = ttk.Label(self, text="Hello World")
        self.label.grid(row=1, column=1)
        self.button = ttk.Button(self, text="Click Me")
        self.button.grid(row=3, column=1)
        # # self.window = Tk()
        # self.window.title("tk Examples")
        # self.window.geometry("500x500")
        # # self.create_widgets()
        # # self.radio_variable = tk.StringVar()
        # # self.combobox_value = tk.StringVar()
        # greeting = ttk.Label(self.window, text="Hello World!")
        # greeting.pack()
    
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller