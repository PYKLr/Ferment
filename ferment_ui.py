#!/usr/bin/env python3

"""
Module for handling the GUI of the Ferment application.

    - Creates a graphical user interface using the tkinter library
    - Allows for Generating, Showing, and Copying Password
    - Does not save the password anywhere!
    - This built around the ideal that you are using a password manager!
"""

__author__ = 'PYKLr'
__date__ = '5/2/2025'

import tkinter as tk
from tkinter import ttk
from ferment_passgen import Passgen
import sys


class Ferment(ttk.Frame):
    """
    A class that represents password generation GUI.

        - Uses tkinter
        - User can specify length, and generate, show, or copy the password
    """

    def __init__(self, master):
        """
        Initialize the Ferment Class.

        Args:
            master (tk.TK): The parent tkinter window
        """
        super().__init__(master)
        self['padding'] = '10 10 10 10'
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        self.passgen = Passgen()
        self.password = tk.StringVar()
        self.showVar = False
        self.length = tk.StringVar()

        self.create_widgets()

    def generate_pass(self):
        """
        Generate a passsword to given length.

        If no length is set, defaults to 16 characters.
        """
        if self.length.get():
            self.passgen.length = int(self.length.get())
        else:
            self.passgen.length = 16
        self.password.set(self.passgen.gen_key())

    def toggle_show(self):
        """Toggle the visibility of the password entry field."""
        self.showVar = not self.showVar
        if self.showVar:
            self.password_entry['show'] = ''
            self.show_button['text'] = 'Hide'
        else:
            self.password_entry['show'] = '*'
            self.show_button['text'] = 'Show'

    def copy_to_clip(self):
        """Copy the currently generated password to clipboard."""
        self.clipboard_clear()
        self.clipboard_append(self.password.get())
        self.update()

    def create_widgets(self):
        """
        Create and arrange widgets on tkinter window.

        Uses:
            - Labels, Entries, and Buttons
        """
        password_label = ttk.Label(self)
        password_label['text'] = 'Password:'
        password_label.grid(row=0, column=0, sticky=tk.E)

        self.password_entry = ttk.Entry(self)
        self.password_entry['width'] = 70
        self.password_entry['textvariable'] = self.password
        self.password_entry['show'] = '*'
        self.password_entry['state'] = 'readonly'
        self.password_entry.grid(row=0, column=1)

        length_label = ttk.Label(self)
        length_label['text'] = 'Length:'
        length_label.grid(row=1, column=0, sticky=tk.E)

        length_entry = ttk.Entry(self)
        length_entry['width'] = 25
        length_entry['textvariable'] = self.length
        length_entry.grid(row=1, column=1)

        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=1)

        gen_button = ttk.Button(button_frame)
        gen_button['text'] = 'Generate'
        gen_button['command'] = self.generate_pass
        gen_button.grid(row=0, column=0)

        copy_button = ttk.Button(button_frame)
        copy_button['text'] = 'Copy'
        copy_button['command'] = self.copy_to_clip
        copy_button.grid(row=0, column=1)

        self.show_button = ttk.Button(button_frame)
        self.show_button['text'] = 'Show'
        self.show_button['command'] = self.toggle_show
        self.show_button.grid(row=0, column=2)

        exit_button = ttk.Button(button_frame)
        exit_button['text'] = 'Exit'
        exit_button['command'] = sys.exit
        exit_button.grid(row=1, column=1)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)


def main():
    """
    Enter the Ferment program.

    Procedure:
        - Initializes tkinter window
        - Initializes Ferment
    """
    root = tk.Tk()
    root.title('Ferment')
    root.geometry('700x200')
    Ferment(root)
    root.mainloop()


if __name__ == '__main__':
    main()
