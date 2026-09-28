from text_stats.analyzer import (
    count_characters,
    count_lines,
    count_words,
    summarize,
)


def test_count_words():
    assert count_words("Python is fun") == 3


def test_count_words_empty_text():
    assert count_words("") == 0


def test_count_characters():
    assert count_characters("abc") == 3


def test_count_lines():
    assert count_lines("first\nsecond") == 2


def test_count_lines_empty_text():
    assert count_lines("") == 0


def test_summarize():
    result = summarize("hello world")

    assert result == {"words": 2, "characters": 11, "lines": 1}
