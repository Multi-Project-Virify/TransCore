from core.engine import TranslationEngine
from modules.tokenizer import Tokenizer
from modules.detector import LanguageDetector
from modules.dictionary import Dictionary
from modules.ranking import Ranking

engine = TranslationEngine()
engine.add_module(Tokenizer())
engine.add_module(LanguageDetector())
engine.add_module(Dictionary())
engine.add_module(Ranking())

result = engine.translate("I went to the river bank")
print(result.result)
# Ожидаем: ... берег (не банк, т.к. "river" рядом)

result2 = engine.translate("I opened a bank account")
print(result2.result)
# Ожидаем: ... банк (не берег, т.к. "account" рядом)