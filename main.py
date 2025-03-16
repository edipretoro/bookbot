import sys

from stats import get_num_words, get_count_characters


def get_book_text(path: str) -> str:
    with open(path, mode="r") as _input:
        content = _input.read()

    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    t = get_book_text(filename)
    num_words = get_num_words(t)
    num_chr = get_count_characters(t)
    alpha_chr = [
        f"{k}: {v}"
        for k, v in num_chr.most_common()
        if k.isalpha()
    ]
    print(f"""============ BOOKBOT ============
Analyzing book found at {filename}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{"\n".join(alpha_chr)}
============= END ==============="""
)


if __name__ == "__main__":
    main()