from modules.detector import LanguageDetector
from core.context import TranslationContext


def test_detect_english():
    ctx = TranslationContext(text="Hello world")
    LanguageDetector().process(ctx)
    assert ctx.source_lang == "en"


def test_detect_russian():
    ctx = TranslationContext(text="Привет мир")
    LanguageDetector().process(ctx)
    assert ctx.source_lang == "ru"