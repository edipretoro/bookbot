from collections import Counter

def get_num_words(text: str) -> int:
    return len(text.split())


def get_count_characters(text: str) -> dict[str, int]:
    c = Counter()
    c.update(list(text.lower()))
    return c