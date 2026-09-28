def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> int:
    return len(text)


def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.splitlines())


def summarize(text: str) -> dict[str, int]:
    return {
        "words": count_words(text),
        "characters": count_characters(text),
        "lines": count_lines(text),
    }
