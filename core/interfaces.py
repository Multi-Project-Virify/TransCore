from typing import Protocol
from core.context import TranslationContext


class Module(Protocol):
    """
    Общий интерфейс для всех модулей движка перевода.
    Любой модуль (tokenizer, detector, dictionary, ranking и т.д.)
    должен реализовывать метод process().
    """

    def process(self, ctx: TranslationContext) -> None:
        ...