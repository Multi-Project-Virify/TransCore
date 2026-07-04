from modules.tokenizer import Tokenizer
from core.context import TranslationContext


def test_tokenizer_basic():
    ctx = TranslationContext(text="Hello, world!")
    Tokenizer().process(ctx)
    assert ctx.tokens == ["Hello", ",", "world", "!"]