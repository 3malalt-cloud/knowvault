# 🔐 KnowVault

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/3malalt-cloud/knowvault/graphs/commit-activity)

**Ein lokaler Link- und Wissensmanager mit verschlüsseltem Tresor** 🚀

KnowVault hilft dir, technische URLs, Dokumentationen und wichtige Links zentral zu verwalten - 100% offline und unter deiner Kontrolle.

---

## 📸 Screenshots

![KnowVault Hauptfenster](docs/screenshots/main-window.png)

---

## ✨ Features

### 🎯 Version 1.0 (Aktuell)

- **📎 Link-Management** - Speichere URLs mit Titel, Kategorie und Tags
- **🔍 Live-Suche** - Echtzeit-Filterung nach Titel, URL, Kategorie oder Tags
- **🗂️ Kategorisierung** - Organisiere Links in beliebigen Kategorien
- **🏷️ Tag-System** - Flexible Verschlagwortung für bessere Auffindbarkeit
- **💾 JSON-Speicherung** - Alle Daten lokal in `data/paths.json`
- **🖱️ Kontextmenü** - Rechtsklick für schnelle Aktionen
- **🌐 Browser-Integration** - Doppelklick öffnet Links direkt
- **🎨 Moderne GUI** - Benutzerfreundliche Tkinter-Oberfläche

### 🚧 Version 1.1 (Geplant)

- 🌙 **Dark Theme** - Toggle zwischen Hell/Dunkel-Modus
- 📤 **Export/Import** - Links als JSON/CSV exportieren
- 🔽 **Kategorien-Filter** - Dropdown zum schnellen Filtern
- ⬆️⬇️ **Sortierung** - Klickbare Spalten-Sortierung
- 📊 **Statistiken** - Dashboard mit Charts und Insights
- 🔒 **Verschlüsselter Tresor** - Sichere Speicherung sensibler Daten

---

## 🚀 Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Setup


Repository klonen

git clone https://github.com/3malalt-cloud/knowvault.git
cd knowvault
Virtuelle Umgebung erstellen

python3 -m venv .venv
Aktivieren (Linux/Mac)

source .venv/bin/activate
Aktivieren (Windows)

.venv\Scriptsctivate
Dependencies installieren

pip install -r requirements.txt

text

---

## 💻 Verwendung

### App starten

python main.py

text

### Link hinzufügen

1. Klicke auf **"+ Link hinzufügen"**
2. Fülle das Formular aus:
   - **Titel**: Name des Links
   - **URL**: Vollständige URL (z.B. `https://github.com`)
   - **Kategorie**: z.B. "Dev", "Docs", "Tools"
   - **Tags**: Kommagetrennt (z.B. `python, tutorial, api`)
3. Klicke **"Hinzufügen"**

### Suchen

- Tippe in die Suchleiste
- Live-Filterung nach Titel, URL, Kategorie oder Tags
- Leere Suche zeigt alle Links

### Link öffnen

- **Doppelklick** auf einen Link → Öffnet im Browser
- **Rechtsklick** → Kontextmenü mit Optionen

### Link löschen

- **Rechtsklick** auf Link → "Löschen"
- Bestätigung erforderlich

---

## 📁 Projektstruktur

knowvault/
├── data/ # Lokale Datenspeicherung
│ └── paths.json # Link-Datenbank (JSON)
├── docs/ # Dokumentation
│ ├── DEVELOPMENT.md # Entwickler-Doku
│ └── screenshots/ # Screenshots
├── knowvault/ # Hauptpaket
│ ├── gui/ # GUI-Komponenten
│ │ ├── widgets/ # Wiederverwendbare Widgets
│ │ │ ├── search_bar.py
│ │ │ ├── link_list.py
│ │ │ └── add_link_dialog.py
│ │ ├── main_window.py # Hauptfenster
│ │ └── styles.py # Design-Konstanten
│ ├── models/ # Datenmodelle
│ │ └── link.py # Link-Klasse
│ └── storage/ # Speicher-Layer
│ └── link_manager.py # JSON-CRUD
├── tests/ # Unit-Tests (geplant)
├── .gitignore
├── main.py # Entry Point
├── README.md
└── requirements.txt

text

---

## 🛠️ Technologie-Stack

- **Python 3.8+** - Programmiersprache
- **Tkinter** - GUI-Framework (Standard-Library)
- **JSON** - Datenspeicherung
- **Dataclasses** - Datenmodellierung
- **MVC-Pattern** - Architektur

---

## 🔒 Sicherheit

- ✅ **100% Offline** - Keine Cloud, kein Tracking
- ✅ **Lokale Speicherung** - Daten bleiben auf deinem Rechner
- ✅ **Keine Dependencies** - Nur Python Standard-Library
- ⏳ **Verschlüsselung** - Geplant für v1.1 (Tresor-Feature)

---

## 🤝 Contributing

Contributions sind willkommen! Bitte:

1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Änderungen (`git commit -m 'Add AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

---

## 📝 Lizenz

Dieses Projekt ist unter der **MIT License** lizenziert - siehe [LICENSE](LICENSE) für Details.

---

## 👨‍💻 Autor

**3malalt-cloud**

- GitHub: [@3malalt-cloud](https://github.com/3malalt-cloud)
- Repository: [knowvault](https://github.com/3malalt-cloud/knowvault)

---

## 🙏 Danksagungen

- Python Community für Tkinter
- Alle Contributors und Tester

---

## 📊 Projekt-Status

![Commits](https://img.shields.io/github/commit-activity/m/3malalt-cloud/knowvault)
![Last Commit](https://img.shields.io/github/last-commit/3malalt-cloud/knowvault)
![Issues](https://img.shields.io/github/issues/3malalt-cloud/knowvault)

**Version:** 1.0.0  
**Status:** ✅ Aktiv in Entwicklung  
**Nächstes Release:** v1.1 mit Dark Theme & Export
