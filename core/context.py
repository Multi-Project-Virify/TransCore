from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TranslationContext:
    """
    Единый объект, который проходит через все модули движка.
    Каждый модуль читает и дополняет его — но никогда не работает
    с другими модулями напрямую.
    """

    # Входные данные
    text: str
    source_lang: Optional[str] = None
    target_lang: Optional[str] = None

    # Промежуточные данные (заполняются модулями по ходу пайплайна)
    tokens: List[str] = field(default_factory=list)
    candidates: Dict[str, List[tuple]] = field(default_factory=dict)
    # candidates: {"bank": [("банк", 0.7), ("берег", 0.3)]}

    # Итог
    result: Optional[str] = None

    # Метаданные / отладка / доп. данные будущих модулей
    meta: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        self.errors.append(message)