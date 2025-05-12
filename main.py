from stats import get_num_words, get_character_count, sort_dictonary_by_count
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])


def print_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")
    character_count = get_character_count(text)
    sorted_character_count = sort_dictonary_by_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_character_count:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


main()
