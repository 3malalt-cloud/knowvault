"""Dialog zum Hinzufügen neuer Links"""
import tkinter as tk
from tkinter import ttk, messagebox
from knowvault.models.link import Link


class AddLinkDialog(tk.Toplevel):
    """Popup-Fenster für neuen Link"""
    
    def __init__(self, parent, on_add_callback):
        super().__init__(parent)
        self.on_add = on_add_callback
        self.result = None
        
        self.title("Link hinzufügen")
        self.geometry("400x280")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        self._create_widgets()
        self.title_entry.focus()
    
    def _create_widgets(self):
        """Erstellt Formular"""
        frame = ttk.Frame(self, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Titel
        ttk.Label(frame, text="Titel:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_entry = ttk.Entry(frame, width=40)
        self.title_entry.grid(row=0, column=1, pady=5, padx=5)
        
        # URL
        ttk.Label(frame, text="URL:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(frame, width=40)
        self.url_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Kategorie
        ttk.Label(frame, text="Kategorie:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.category_entry = ttk.Entry(frame, width=40)
        self.category_entry.insert(0, "Allgemein")
        self.category_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Tags
        ttk.Label(frame, text="Tags:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.tags_entry = ttk.Entry(frame, width=40)
        self.tags_entry.grid(row=3, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(kommagetrennt)", font=('Segoe UI', 8)).grid(
            row=4, column=1, sticky=tk.W
        )
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)
        
        ttk.Button(btn_frame, text="Hinzufügen", command=self._add_link).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(btn_frame, text="Abbrechen", command=self.destroy).pack(
            side=tk.LEFT, padx=5
        )
    
    def _add_link(self):
        """Validiert und erstellt Link"""
        title = self.title_entry.get().strip()
        url = self.url_entry.get().strip()
        category = self.category_entry.get().strip() or "Allgemein"
        tags_str = self.tags_entry.get().strip()
        
        if not title or not url:
            messagebox.showerror("Fehler", "Titel und URL sind erforderlich!")
            return
        
        tags = [t.strip() for t in tags_str.split(',') if t.strip()]
        
        link = Link(
            title=title,
            url=url,
            category=category,
            tags=tags
        )
        
        self.on_add(link)
        self.destroy()
