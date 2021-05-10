from pathlib import Path
from discord import File

path = Path(r"./memebase/")

def list_memes(theme: str) -> list:
    p = path/theme
    l = list()
    if not p.exists():
        return l

    for i in p.iterdir():
        l.append(i.name)

    return l


def list_themes() -> list:
    return [i.name for i in path.iterdir()]


def get_meme(theme: str, name: str):
    p = path/theme/name
    if not p.exists():
        return None
    return File(str(p))
