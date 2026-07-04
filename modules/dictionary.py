import json
from pathlib import Path
from core.context import TranslationContext

_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "dict_en_ru.json"


class Dictionary:
    def __init__(self, data_path: Path = _DATA_PATH):
        with open(data_path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

    def process(self, ctx: TranslationContext) -> None:
        for token in ctx.tokens:
            key = token.lower()
            if key in self._data:
                ctx.candidates[key] = [
                    (entry["translation"], entry["weight"], entry["context"])
                    for entry in self._data[key]
                ]