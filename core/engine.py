from typing import List
from core.context import TranslationContext
from core.interfaces import Module


class TranslationEngine:
    """
    Движок ничего не знает про конкретные языки или алгоритмы перевода.
    Он только последовательно прогоняет TranslationContext через
    зарегистрированные модули.
    """

    def __init__(self) -> None:
        self._modules: List[Module] = []

    def add_module(self, module: Module) -> "TranslationEngine":
        self._modules.append(module)
        return self

    def translate(
        self,
        text: str,
        source_lang: str | None = None,
        target_lang: str | None = None,
    ) -> TranslationContext:
        ctx = TranslationContext(
            text=text,
            source_lang=source_lang,
            target_lang=target_lang,
        )

        for module in self._modules:
            try:
                module.process(ctx)
            except Exception as e:
                ctx.add_error(f"{module.__class__.__name__}: {e}")

        return ctx