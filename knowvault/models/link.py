"""Link-Datenmodell für KnowVault"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Link:
    """Repräsentiert einen gespeicherten Link"""
    title: str
    url: str
    category: str = "Allgemein"
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def matches_search(self, query: str) -> bool:
        """Prüft ob Link zur Suchanfrage passt"""
        query = query.lower()
        return (
            query in self.title.lower() or
            query in self.url.lower() or
            query in self.category.lower() or
            any(query in tag.lower() for tag in self.tags)
        )
    
    def to_dict(self) -> dict:
        """Konvertiert zu Dictionary für JSON"""
        return {
            'title': self.title,
            'url': self.url,
            'category': self.category,
            'tags': self.tags,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Link':
        """Erstellt Link aus Dictionary"""
        return cls(**data)
