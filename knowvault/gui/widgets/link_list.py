"""Link-Tabelle mit Treeview"""
import tkinter as tk
from tkinter import ttk
import webbrowser


class LinkList(ttk.Frame):
    """Treeview-basierte Link-Liste"""
    
    def __init__(self, parent, on_delete_callback):
        super().__init__(parent)
        self.on_delete = on_delete_callback
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            self,
            columns=('title', 'url', 'category', 'tags'),
            show='headings',
            yscrollcommand=scrollbar.set,
            height=20
        )
        
        # Spalten konfigurieren
        self.tree.heading('title', text='Titel')
        self.tree.heading('url', text='URL')
        self.tree.heading('category', text='Kategorie')
        self.tree.heading('tags', text='Tags')
        
        self.tree.column('title', width=200)
        self.tree.column('url', width=300)
        self.tree.column('category', width=120)
        self.tree.column('tags', width=150)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Events
        self.tree.bind('<Double-1>', self._open_link)
        self.tree.bind('<Button-3>', self._show_context_menu)
        
        # Kontextmenü
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Öffnen", command=self._open_selected)
        self.context_menu.add_command(label="Löschen", command=self._delete_selected)
    
    def update_links(self, links):
        """Aktualisiert die Anzeige"""
        self.tree.delete(*self.tree.get_children())
        for link in links:
            tags_str = ', '.join(link.tags) if link.tags else '-'
            self.tree.insert('', tk.END, values=(
                link.title,
                link.url,
                link.category,
                tags_str
            ))
    
    def _open_link(self, event):
        """Öffnet Link im Browser bei Doppelklick"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            url = item['values'][1]
            webbrowser.open(url)
    
    def _show_context_menu(self, event):
        """Zeigt Rechtsklick-Menü"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def _open_selected(self):
        """Öffnet ausgewählten Link"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            webbrowser.open(item['values'][1])
    
    def _delete_selected(self):
        """Löscht ausgewählten Link"""
        selection = self.tree.selection()
        if selection:
            index = self.tree.index(selection[0])
            self.on_delete(index)
