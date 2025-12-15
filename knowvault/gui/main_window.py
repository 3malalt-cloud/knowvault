"""KnowVault - Hauptfenster"""
import tkinter as tk
from tkinter import ttk, messagebox
from knowvault.storage.link_manager import LinkManager
from knowvault.gui.widgets.search_bar import SearchBar
from knowvault.gui.widgets.link_list import LinkList
from knowvault.gui.widgets.add_link_dialog import AddLinkDialog


class KnowVaultApp(tk.Tk):
    """Haupt-Anwendungsfenster"""
    
    def __init__(self):
        super().__init__()
        
        self.title("KnowVault - Link Manager")
        self.geometry("900x600")
        
        # Storage initialisieren
        self.link_manager = LinkManager()
        
        # GUI erstellen
        self._create_widgets()
        self._refresh_links()
    
    def _create_widgets(self):
        """Erstellt alle GUI-Komponenten"""
        # Toolbar
        toolbar = ttk.Frame(self, padding=10)
        toolbar.pack(fill=tk.X)
        
        # Suchleiste
        self.search_bar = SearchBar(toolbar, self._on_search)
        self.search_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Add-Button
        add_btn = ttk.Button(
            toolbar,
            text="+ Link hinzufügen",
            command=self._show_add_dialog
        )
        add_btn.pack(side=tk.RIGHT, padx=5)
        
        # Link-Liste
        list_frame = ttk.Frame(self, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.link_list = LinkList(list_frame, self._on_delete)
        self.link_list.pack(fill=tk.BOTH, expand=True)
        
        # Statusleiste
        self.status_bar = ttk.Label(
            self,
            text=f"Gespeicherte Links: {len(self.link_manager.get_all_links())}",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def _refresh_links(self, links=None):
        """Aktualisiert Link-Anzeige"""
        if links is None:
            links = self.link_manager.get_all_links()
        
        self.link_list.update_links(links)
        self.status_bar.config(
            text=f"Gespeicherte Links: {len(self.link_manager.get_all_links())} | "
                 f"Angezeigt: {len(links)}"
        )
    
    def _on_search(self, query):
        """Führt Suche aus"""
        if query and query != "Suche nach Titel, URL, Tags...":
            results = self.link_manager.search_links(query)
            self._refresh_links(results)
        else:
            self._refresh_links()
    
    def _show_add_dialog(self):
        """Zeigt Dialog zum Link hinzufügen"""
        AddLinkDialog(self, self._on_add_link)
    
    def _on_add_link(self, link):
        """Fügt neuen Link hinzu"""
        if self.link_manager.add_link(link):
            self._refresh_links()
            messagebox.showinfo("Erfolg", f"Link '{link.title}' hinzugefügt!")
        else:
            messagebox.showerror("Fehler", "Link konnte nicht gespeichert werden!")
    
    def _on_delete(self, index):
        """Löscht Link"""
        if messagebox.askyesno("Löschen", "Link wirklich löschen?"):
            if self.link_manager.delete_link(index):
                self._refresh_links()
                messagebox.showinfo("Erfolg", "Link gelöscht!")


def main():
    """Startet die Anwendung"""
    app = KnowVaultApp()
    app.mainloop()


if __name__ == "__main__":
    main()
