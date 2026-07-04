import re
from core.context import TranslationContext

_CYRILLIC = re.compile(r"[а-яА-ЯёЁ]")
_LATIN = re.compile(r"[a-zA-Z]")


class LanguageDetector:
    """
    Простое локальное определение языка по алфавиту.
    Для en/ru этого достаточно — никаких внешних сервисов,
    весь анализ происходит на устройстве.
    """

    def process(self, ctx: TranslationContext) -> None:
        if ctx.source_lang:
            return  # язык уже задан явно

        cyrillic_count = len(_CYRILLIC.findall(ctx.text))
        latin_count = len(_LATIN.findall(ctx.text))

        if cyrillic_count > latin_count:
            ctx.source_lang = "ru"
        elif latin_count > 0:
            ctx.source_lang = "en"
        else:
            ctx.add_error("Не удалось определить язык")