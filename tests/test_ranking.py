from modules.ranking import Ranking
from core.context import TranslationContext


def test_ranking_picks_context_word():
    ctx = TranslationContext(text="")
    ctx.tokens = ["river", "bank"]
    ctx.candidates = {
        "bank": [
            ("банк", 0.6, ["account", "money"]),
            ("берег", 0.4, ["river", "water"]),
        ]
    }
    Ranking().process(ctx)
    assert "берег" in ctx.result