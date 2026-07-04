from core.context import TranslationContext


class Ranking:
    """
    Выбирает лучшего кандидата для каждого слова, учитывая
    соседние слова в тексте (простой контекстный анализ).
    """

    def process(self, ctx: TranslationContext) -> None:
        tokens_lower = [t.lower() for t in ctx.tokens]
        translated_words = []

        for i, token in enumerate(ctx.tokens):
            key = token.lower()
            candidates = ctx.candidates.get(key)

            if not candidates:
                translated_words.append(token)
                continue

            neighbors = set(tokens_lower[max(0, i - 3):i] + tokens_lower[i + 1:i + 4])

            best = None
            best_score = -1.0

            for translation, weight, context_words in candidates:
                score = weight
                if neighbors & set(context_words):
                    score += 1.0  # совпадение с контекстом сильно поднимает вес

                if score > best_score:
                    best_score = score
                    best = translation

            translated_words.append(best)

        ctx.result = " ".join(translated_words)