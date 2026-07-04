import re
from core.context import TranslationContext


class Tokenizer:
    """
    Разбивает входной текст на токены (слова, знаки препинания).
    Простая regex-версия — без сторонних библиотек и без отправки
    текста куда-либо, всё работает локально.
    """

    _TOKEN_PATTERN = re.compile(r"\w+|[^\w\s]", re.UNICODE)

    def process(self, ctx: TranslationContext) -> None:
        ctx.tokens = self._TOKEN_PATTERN.findall(ctx.text)