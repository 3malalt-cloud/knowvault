"""
KnowVault GUI - Hauptfenster
"""
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser


class KnowVaultGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KnowVault - Link & Secret Manager")
        self.root.geometry("900x700")
        
        # Header
        header = ttk.Label(
            self.root, 
            text="🔐 KnowVault", 
            font=("Arial", 20, "bold")
        )
        header.pack(pady=20)
        
        # Eingabebereich
        self.create_input_section()
        
        # Suchbereich
        self.create_search_section()
        
    def create_input_section(self):
        """Eingabefelder für neue Links"""
        frame = ttk.LabelFrame(self.root, text="Neuen Link hinzufügen", padding=10)
        frame.pack(padx=20, pady=10, fill="x")
        
        # Titel
        ttk.Label(frame, text="Titel:").grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = ttk.Entry(frame, width=50)
        self.title_entry.grid(row=0, column=1, pady=5, padx=5)
        
        # URL
        ttk.Label(frame, text="URL:").grid(row=1, column=0, sticky="w", pady=5)
        self.url_entry = ttk.Entry(frame, width=50)
        self.url_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Wegbeschreibung
        ttk.Label(frame, text="Weg:").grid(row=2, column=0, sticky="w", pady=5)
        self.path_entry = ttk.Entry(frame, width=50)
        self.path_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Speichern-Button
        save_btn = ttk.Button(frame, text="💾 Speichern", command=self.save_link)
        save_btn.grid(row=3, column=1, pady=10, sticky="e")
        
    def create_search_section(self):
        """Suchfeld und Ergebnisliste"""
        frame = ttk.LabelFrame(self.root, text="Links suchen & öffnen", padding=10)
        frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Suchfeld
        search_frame = ttk.Frame(frame)
        search_frame.pack(fill="x", pady=5)
        
        ttk.Label(search_frame, text="🔍 Suche:").pack(side="left")
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        # Liste mit besseren Farben
        self.results_list = tk.Listbox(
            frame, 
            height=12, 
            selectmode=tk.SINGLE, 
            cursor="hand2",
            bg="white",
            selectbackground="#0078D4",
            selectforeground="white"
        )
        self.results_list.pack(fill="both", expand=True, pady=5)
        
        # Doppelklick zum Öffnen
        self.results_list.bind("<Double-Button-1>", lambda e: self.open_link())
        
        # Button-Leiste
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=5)
        
        open_btn = ttk.Button(btn_frame, text="🌐 Link öffnen", command=self.open_link)
        open_btn.pack(side="left", padx=5)
        
        delete_btn = ttk.Button(btn_frame, text="🗑️ Löschen", command=self.delete_link)
        delete_btn.pack(side="left", padx=5)
        
    def save_link(self):
        """Link speichern"""
        title = self.title_entry.get().strip()
        url = self.url_entry.get().strip()
        path = self.path_entry.get().strip()
        
        if not title or not url:
            messagebox.showwarning("Fehlende Daten", "Titel und URL müssen ausgefüllt sein!")
            return
        
        # Zur Liste hinzufügen
        display_text = f"{title} - {url}"
        if path:
            display_text += f" (Weg: {path})"
        
        self.results_list.insert(tk.END, display_text)
        
        # Felder leeren
        self.title_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)
        self.path_entry.delete(0, tk.END)
        
        print(f"✅ Gespeichert: {title} -> {url}")
        
    def open_link(self):
        """Link im Browser öffnen"""
        selection = self.results_list.curselection()
        
        if not selection:
            messagebox.showinfo("Keine Auswahl", "Bitte wähle zuerst einen Link aus der Liste!")
            return
        
        text = self.results_list.get(selection[0])
        print(f"📝 Ausgewählter Eintrag: {text}")
        
        # URL extrahieren
        if " - " in text:
            parts = text.split(" - ", 1)
            url_part = parts[1]
            
            # Wegbeschreibung entfernen falls vorhanden
            if " (Weg:" in url_part:
                url = url_part.split(" (Weg:")[0].strip()
            else:
                url = url_part.strip()
            
            print(f"🌐 Öffne: {url}")
            webbrowser.open(url)
        else:
            messagebox.showerror("Fehler", "URL-Format nicht erkannt!")
    
    def delete_link(self):
        """Ausgewählten Link löschen"""
        selection = self.results_list.curselection()
        
        if not selection:
            messagebox.showinfo("Keine Auswahl", "Bitte wähle zuerst einen Link zum Löschen!")
            return
        
        # Bestätigung
        text = self.results_list.get(selection[0])
        title = text.split(" - ")[0] if " - " in text else text
        
        confirm = messagebox.askyesno(
            "Löschen bestätigen", 
            f"Möchtest du '{title}' wirklich löschen?"
        )
        
        if confirm:
            self.results_list.delete(selection[0])
            print(f"🗑️ Gelöscht: {title}")
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = KnowVaultGUI()
    app.run()
