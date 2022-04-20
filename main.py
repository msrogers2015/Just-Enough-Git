#!/usr/bin/env python3

import os
import shutil
import tkinter as tk
import webbrowser
from commands import gui
from data import tkinter_values as tv


class App(tk.Frame):
    def __init__(self, root=None):
        # Setting up GUI window for rendering
        super().__init__(root)
        self.root = root
        # Rendering app menu and main window.
        self.gui = gui.GUI(self.root)
        # Activating key bindings
        self.key_bindings()
        # SEtting home path for future referencing
        tv.home_path = os.getcwd()

    def key_bindings(self):
        """Creation of useful shortcut commands using various key
        combination bindings"""
        self.root.bind("<Control-o>", self.gui.setup_commands.init_repo)
        self.root.bind("<Control-O>", self.gui.setup_commands.clone_repo)
        self.root.bind("<Control-c>", self.gui.stage_commands.output_files)
        self.root.bind("<Control-s>", self.gui.stage_commands.commit)
        self.root.bind("<Control-S>", self.gui.stage_commands.quick_commit)
        self.root.bind("<Control-p>", self.gui.stage_commands.push)
        self.root.bind("<Control-P>", self.gui.stage_commands.pull)
        self.root.bind("<Control-b>", self.gui.branch_commands.branches)
        self.root.bind("<Control-m>", self.gui.branch_commands.merge_branch)


if __name__ == "__main__":
    # If git isn't installed, create a window linking to git website
    if shutil.which("git") is None:
        root = tk.Tk()
        root.title("Git Not Found")
        root.geometry("300x100")
        error_label = tk.Label(root, text="Please install git",
                               font=("Arial", 18))
        get_git_btn = tk.Button(
            root,
            text="Get Git",
            command=lambda: webbrowser.open("https://git-scm.com/downloads"),
            font=("Arial", 14),
        )
        error_label.pack()
        get_git_btn.pack()
        root.mainloop()
    # IF git is installed, create an instance of the application and run it
    else:
        root = tk.Tk()
        root.geometry(f"{tv.width}x{tv.height}")
        root.title("GitPy")
        root.resizable(False, False)
        app = App(root=root)
        app.mainloop()
