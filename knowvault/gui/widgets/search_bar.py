"""Suchleiste mit Live-Suche"""
import tkinter as tk
from tkinter import ttk


class SearchBar(ttk.Frame):
    """Suchfeld mit Echtzeit-Filterung"""
    
    def __init__(self, parent, on_search_callback):
        super().__init__(parent)
        self.on_search = on_search_callback
        
        # Suchicon-Label (Unicode)
        self.icon_label = ttk.Label(self, text="🔍", font=('Segoe UI', 12))
        self.icon_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # Eingabefeld
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self.on_search(self.search_var.get()))
        
        self.entry = ttk.Entry(
            self, 
            textvariable=self.search_var,
            font=('Segoe UI', 10),
            width=40
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry.insert(0, "Suche nach Titel, URL, Tags...")
        
        # Placeholder-Effekt
        self.entry.bind('<FocusIn>', self._clear_placeholder)
        self.entry.bind('<FocusOut>', self._restore_placeholder)
    
    def _clear_placeholder(self, event):
        if self.search_var.get() == "Suche nach Titel, URL, Tags...":
            self.search_var.set("")
    
    def _restore_placeholder(self, event):
        if not self.search_var.get():
            self.search_var.set("Suche nach Titel, URL, Tags...")
