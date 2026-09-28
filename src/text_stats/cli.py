import argparse

from text_stats.analyzer import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate basic statistics for text.")

    parser.add_argument("text", help="Text to analyze.")

    args = parser.parse_args()

    stats = summarize(args.text)

    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print(f"Lines: {stats['lines']}")
