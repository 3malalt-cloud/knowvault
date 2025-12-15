"""
KnowVault GUI - Hauptfenster
"""
import tkinter as tk
from tkinter import ttk

class KnowVaultGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KnowVault - Link & Secret Manager")
        self.root.geometry("800x600")
        
        # Header
        header = ttk.Label(
            self.root, 
            text="🔐 KnowVault", 
            font=("Arial", 20, "bold")
        )
        header.pack(pady=20)
        
        # Info
        info = ttk.Label(
            self.root,
            text="Dein lokaler Link-Manager mit verschlüsseltem Tresor"
        )
        info.pack()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KnowVaultGUI()
    app.run()
