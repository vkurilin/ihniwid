import urllib.parse
from typing import Optional

__all__ = ("Question",)


class Question:
    def __init__(self, *, url: str, text: str):
        self.text = text
        self.url = url

    def id(self) -> Optional[int]:
        parsed = urllib.parse.urlparse(self.url)
        if parsed.hostname and parsed.hostname != "stackoverflow.com":
            return None
        parts: list[str] = parsed.path.split("/")
        if len(parts) < 3:
            return None
        if parts[0] != "" or parts[1] != "questions":
            return None
        return int(parts[2])
