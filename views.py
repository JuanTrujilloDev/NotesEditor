import tkinter as tk
from tkinter import ttk
from typing import Any

import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self, *args: Any, **kwargs: Any):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.title("Notepad")
        self.geometry("900x600")
        self.resizable(True, True)
        self.minsize(700, 500)


class FileMenu(tk.Menu):
    def __init__(self, *args: Any, **kwargs: Any):
        super(FileMenu, self).__init__()
        self.config(tearoff=0)  # type: ignore
        self.add_command(label="New")
        self.add_command(label="Open")
        self.add_command(label="Save")
        self.add_command(label="Save As")
        self.add_separator()
        self.add_command(label="Exit", command=self.quit)


class Menu(tk.Menu):
    def __init__(self, *args: Any, **kwargs: Any):
        super(Menu, self).__init__()
        self.add_cascade(label="File", menu=FileMenu(self))
        self.add_command(label="Edit")
        self.add_command(label="View")
        self.add_command(label="Help")


class InputBox(ctk.CTkTextbox):
    def __init__(self, *args: Any, **kwargs: Any):
        super(InputBox, self).__init__(*args, **kwargs)
        self._font = "Arial", 15
        self._corner_radius = 0
        self.pack(fill="both", expand=True)


class BottomBox(ctk.CTkFrame):
    def __init__(self, *args: Any, **kwargs: Any):
        super(BottomBox, self).__init__(*args, **kwargs)
        self._corner_radius = 0
        self.columnconfigure(0, weight=1)
        self.pack(fill="x", side="bottom")


class WordsLengthLabel(ctk.CTkLabel):
    def __init__(self, *args: Any, **kwargs: Any):
        super(WordsLengthLabel, self).__init__(*args, **kwargs)
        self._anchor = "w"
        self._font = ("Arial", 14)
        self.grid(column=0, row=0, sticky="w", padx=(20, 70))


class SeparatorInfo(ttk.Separator):
    def __init__(self, *args: Any, **kwargs: Any):
        super(SeparatorInfo, self).__init__(*args, **kwargs)
        self.config(orient=tk.VERTICAL)
        self.grid(row=0, column=2, ipady=20, sticky=tk.EW)


class OperativeSystemLabel(ctk.CTkLabel):
    def __init__(self, *args: Any, **kwargs: Any):
        super(OperativeSystemLabel, self).__init__(*args, **kwargs)
        self._anchor = "w"
        self._justify = "left"
        self._font = ("Arial", 14)
        self.grid(column=3, row=0, sticky="W", padx=(10, 20))
