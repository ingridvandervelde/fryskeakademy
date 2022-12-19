from nltk.util import trigrams
from conllu import parse
from collections import Counter


def is_conllu_ext(filename: str) -> bool:
    return True if filename[-6:] == 'conllu' else False


def conllu_to_counter(filename: str) -> Counter:
    with open(filename, 'r', encoding="utf8") as f:
        sentences = parse(f.read())

    trigram_counter = Counter()

    for sentence in sentences:
        trigram_counter.update(trigrams([item['upos'] for item in sentence]))

    return trigram_counter
