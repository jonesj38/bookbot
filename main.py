from stats import get_num_words, get_char_counts, sort_char_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = get_num_words(book)
    char_counts = get_char_counts(book)
    sorted_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

main()
