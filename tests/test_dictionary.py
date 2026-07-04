from modules.dictionary import Dictionary
from core.context import TranslationContext


def test_dictionary_finds_candidates():
    ctx = TranslationContext(text="bank")
    ctx.tokens = ["bank"]
    Dictionary().process(ctx)
    assert "bank" in ctx.candidates
    assert len(ctx.candidates["bank"]) > 0