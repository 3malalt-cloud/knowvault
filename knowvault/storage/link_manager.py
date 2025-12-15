"""Link-Speicherung und -Verwaltung"""
import json
from pathlib import Path
from typing import List, Optional
from knowvault.models.link import Link


class LinkManager:
    """Verwaltet Links mit JSON-Speicherung"""
    
    def __init__(self, data_path: str = "data/paths.json"):
        self.data_path = Path(data_path)
        self.links: List[Link] = []
        self.load_links()
    
    def load_links(self) -> None:
        """Lädt Links aus JSON-Datei"""
        if not self.data_path.exists():
            return
        
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.links = [Link.from_dict(item) for item in data.get('links', [])]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Fehler beim Laden: {e}")
            self.links = []
    
    def save_links(self) -> bool:
        """Speichert Links in JSON-Datei"""
        try:
            data = {
                'links': [link.to_dict() for link in self.links],
                'metadata': {
                    'version': '1.0',
                    'total_links': len(self.links)
                }
            }
            
            self.data_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False
    
    def add_link(self, link: Link) -> bool:
        """Fügt neuen Link hinzu"""
        self.links.append(link)
        return self.save_links()
    
    def delete_link(self, index: int) -> bool:
        """Löscht Link an Index"""
        if 0 <= index < len(self.links):
            del self.links[index]
            return self.save_links()
        return False
    
    def search_links(self, query: str) -> List[Link]:
        """Sucht Links nach Query"""
        if not query:
            return self.links
        return [link for link in self.links if link.matches_search(query)]
    
    def get_all_links(self) -> List[Link]:
        """Gibt alle Links zurück"""
        return self.links.copy()
